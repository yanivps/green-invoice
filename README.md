# Green Invoice API

> A Python 3 module to interact with the Green Invoice API.

## Install

```sh
pip install green-invoice
```

## Example

```python
from datetime import datetime
import logging
import green_invoice
from green_invoice.models import (
    Currency,
    DocumentLanguage,
    DocumentType,
    PaymentCardType,
    PaymentDealType,
    PaymentType,
    IncomeVatType,
)
from green_invoice.resources import DocumentResource


def main():
    green_invoice.client.configure(
        env="sandbox",
        # Authentication
        api_key_id="YOUR_API_KEY_ID",
        api_key_secret="YOUR_API_KEY_SECRET",
        # Logger
        logger=logging.root,
    )

    order_amount = 50
    order_amount_currency = Currency.USD
    create_document_for_order(order_amount, order_amount_currency)


def create_document_for_order(amount, amount_currency):
    documentResource = DocumentResource()
    created_document = documentResource.create(
        {
            "type": DocumentType.TAX_INVOICE_RECEIPT,
            "client": {
                "name": "Tom Hanks",
                "add": False,
            },
            "currency": amount_currency,
            "lang": DocumentLanguage.ENGLISH,
            "signed": True,
            "rounding": False,
            "income": [
                {
                    "price": amount,
                    "currency": amount_currency,
                    "quantity": 1,
                    "description": "My Cool Product",
                    "vatType": IncomeVatType.INCLUDED,
                }
            ],
            "payment": [
                {
                    "type": PaymentType.CREDIT_CARD,
                    "date": datetime.today().strftime("%Y-%m-%d"),
                    "dealType": PaymentDealType.REGULAR,
                    "cardNum": "4242",
                    "cardType": PaymentCardType.VISA,
                    "price": amount,
                    "currency": amount_currency,
                }
            ],
        }
    )
    print(created_document)


if __name__ == "__main__":
    main()

```

## Author

**Yaniv Pinchas**

* [github/yanivps](https://github.com/yanivps)


