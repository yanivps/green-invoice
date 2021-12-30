import json
import requests
from logging import Logger
from .exceptions import (
    ImproperlyConfigured,
    APIError,
    CardError,
    AuthenticationError,
)


def default_user_agent():
    """
    Generate default user agent based on library repo name, Python version and requests version
    :return: string
    """
    import platform
    from .version import __version__

    library_versions = "requests {}; python {}".format(
        requests.__version__, platform.version()
    )
    return "mayple/bluesnap {} ({})".format(__version__, library_versions)


def format_request(req):
    return "\n".join(
        [
            "%s %s" % (req.method, req.url),
            "\n".join("%s: %s" % (k, v) for k, v in req.headers.items()),
            "",
            req.body or "",
        ]
    )


def format_response(res):
    return "\n".join(
        [
            "%d %s" % (res.status_code, res.reason or ""),
            "\n".join("%s: %s" % (k, v) for k, v in res.headers.items()),
            "",
            res.text,
        ]
    )


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class Client(object):
    ENDPOINTS = {
        "live": "https://api.greeninvoice.co.il/api",
        "sandbox": "https://sandbox.d.greeninvoice.co.il/api",
    }

    def __init__(
        self,
        # Environment
        env,
        # Authentication
        api_key_id,
        api_key_secret,
        # Logger
        logger=None,
    ):
        if env not in self.ENDPOINTS:
            raise ValueError("env not in {0}".format(self.ENDPOINTS.keys()))

        self.env = env
        self.api_key_id = api_key_id
        self.api_key_secret = api_key_secret

        self.logger = logger if isinstance(logger, Logger) else None

        self.last_response = None

    @property
    def endpoint_url(self):
        return self.ENDPOINTS[self.env]

    @property
    def http_bearer_auth(self):
        authenticate_url = self.ENDPOINTS[self.env] + "/v1/account/token"
        response = requests.post(
            authenticate_url,
            json={"id": self.api_key_id, "secret": self.api_key_secret},
        )
        jwt_token = response.headers.get("X-Authorization-Bearer")
        if not response.ok or not jwt_token:
            raise AuthenticationError()
        return BearerAuth(jwt_token)

    def request(self, method, path, data=None):
        """
        API request method

        :param method: HTTP method
        :param path: URL path
        :param data: json data as dictionary
        :return:
        """
        url = self.endpoint_url + path

        dataString = None
        if type(data) == dict:
            dataString = json.dumps(data)

        headers = {"Content-Type": "application/json"}

        # Prepare request
        req = requests.Request(
            method, url, headers, data=dataString, auth=self.http_bearer_auth
        )
        r = req.prepare()

        if self.logger:
            self.logger.info("GreenInvoice request:\n%s", format_request(r))

        # Send request, returning response
        s = requests.Session()
        response = s.send(r)

        if self.logger:
            self.logger.info(
                "GreenInvoice response (took %s):\n%s",
                response.elapsed,
                format_response(response),
            )

        # Save request and response for further logging
        self.last_response = response

        body = self._process_response_body(response)

        return response, body

    def _process_response_body(self, response):
        body = None

        if response.content:  # There's content, parse it as XML
            responseContent = response.content
            if type(response.content) == bytes:
                responseContent = response.content.decode("utf-8")

            try:
                body = json.loads(responseContent)
            except Exception:
                # Cannot parse body as JSON, could be a text
                raise APIError(
                    description=responseContent, status_code=response.status_code
                )

        if not (200 <= response.status_code < 300):
            self._handle_api_error(response, body)

        return body

    # noinspection PyMethodMayBeStatic
    def _handle_api_error(self, response, body):
        """
        Try to find the error message and raise the correct exception
        :raises APIError
        :param response: HTTP response
        :param body: Messages may contain in <xml/> or <messages><message/></messages>
        """

        description = None

        if not body:
            description = "<no response body>"
        elif not isinstance(body, dict):
            description = body
        else:
            body = {"messages": body}

        if description:
            raise APIError(description=description, status_code=response.status_code)

        try:  # <messages><message><description>message</description></message></messages>
            if isinstance(
                body.get("messages", {}).get("message", None), list
            ):  # Multiple <message/> elements
                raise APIError(
                    messages=body["messages"]["message"],
                    status_code=response.status_code,
                )
            else:  # Only 1 <message/> element
                code = body.get("messages", {}).get("message", {}).get("code", None)

                raise APIError(
                    description=body["messages"]["message"]["description"],
                    code=code,
                    status_code=response.status_code,
                )

        except APIError:
            raise
        except Exception:
            raise APIError(
                description="Invalid messages object in response from API: {body}".format(
                    body=body
                ),
                status_code=response.status_code,
            )


__client__ = None


def default():
    """:rtype : Client"""
    global __client__

    if __client__ is None:
        raise ImproperlyConfigured(
            "GreenInvoice client not configured yet. Please call green_invoice.client.configure()."
        )

    return __client__


def configure(**config):
    """:rtype : Client"""
    global __client__

    __client__ = Client(**config)

    return __client__
