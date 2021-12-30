import re
from abc import abstractmethod
from typing import List, Optional
from urllib.parse import urlparse

import requests
from lxml import etree

from . import models
from .client import default as default_client


class Resource(object):
    def __init__(self, client=None):
        self.client = client or default_client()
        """:type : .client.Client"""

    def request(self, method, path, data=None):
        response, body = self.client.request(method, path, data)
        return response, body


class ClientResource(Resource):
    clients_path = "/v1/clients"
    client_path = clients_path + "/{client_id}"
    client_id_path_pattern = re.compile(
        r"{}/(\d+)".format(clients_path)
    )  # /v1/clients/(\d+)

    def find_by_client_id(self, client_id) -> models.IClient:
        """
        :param client_id: Green Invoice client id
        :return: client dictionary
        """
        response, body = self.request(
            "GET", self.client_path.format(client_id=client_id)
        )
        return body

    def search_client(
        self, params: models.IClientSearchFields
    ) -> models.IClientSearchResult:
        """
        :param params: Green Invoice client search params
        :return: clients search results dictionary
        """
        response, body = self.request(
            "POST", self.clients_path + "/search", data=params
        )
        return body

    def create(self, client_params: models.IClientDraft) -> models.IClient:
        """
        Creates a new client
        :param client_params:
        :return: Returns the newly created Green Invoice client
        """

        response, body = self.request("POST", self.clients_path, data=client_params)

        return body

    def update(self, client_id: str, client_params: models.IClientDraft):
        """
        Updates an existing client
        :param client_id: Green Invoice client id
        :param client_params:
        :return: Returns the updated Green Invoice client
        """

        response, body = self.request(
            "PUT", self.client_path.format(client_id=client_id), data=client_params
        )
        return body

    def delete(self, client_id: str):
        """
        Deletes an existing client
        :param client_id: Green Invoice client id
        :return: Returns the deleted Green Invoice client
        """

        response, body = self.request(
            "DELETE", self.client_path.format(client_id=client_id)
        )
        return body

    def associate_documents(self, client_id: str, document_ids: List[str]):
        data = {"ids": document_ids}
        response, _ = self.request(
            "POST", self.client_path.format(client_id=client_id) + "/assoc", data=data
        )
        return response.ok


class DocumentResource(Resource):
    documents_path = "/v1/documents"
    document_path = documents_path + "/{document_id}"
    document_id_path_pattern = re.compile(
        r"{}/(\d+)".format(documents_path)
    )  # /v1/clients/(\d+)

    def find_by_document_id(self, document_id) -> models.IClient:
        """
        :param document_id: Green Invoice client id
        :return: client dictionary
        """
        response, body = self.request(
            "GET", self.document_path.format(document_id=document_id)
        )
        return body

    def search_document(
        self, params: models.IDocumentSearchFields
    ) -> models.IDocumentSearchResult:
        """
        :param params: Green Invoice document search params
        :return: documents search results dictionary
        """
        response, body = self.request(
            "POST", self.documents_path + "/search", data=params
        )
        return body

    def create(self, document_params: models.IDocumentDraft) -> models.IDocument:
        """
        Creates a new document
        :param document_params:
        :return: Returns the newly created Green Invoice document
        """

        response, body = self.request("POST", self.documents_path, data=document_params)

        return body

    def get_document_download_link(self, document_id: str) -> models.IDocumentUrl:
        """
        Gets document's download link as IDocumentUrl
        :param document_id: Green Invoice document id
        :return: Returns the IDocumentUrl of a Green Invoice document
        """

        response, body = self.request(
            "GET",
            self.document_path.format(document_id=document_id) + "/download/links",
        )
        return body
