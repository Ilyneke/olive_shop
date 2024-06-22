import uuid
import requests

from settings.base import SHOP_ID, SHOP_SECRET_KEY


def create_payment(price: str, currency: str, return_url, description: str):
    yookassa_api_endpoint = 'https://api.yookassa.ru/v3/payments'
    unic_id = uuid.uuid4()
    payment = requests.post(
        url=yookassa_api_endpoint,
        auth=(SHOP_ID, SHOP_SECRET_KEY),
        headers={
            'Idempotence-Key': str(unic_id),
            'Content-Type': 'application/json',
        },
        json={
            "amount": {
                "value": price,
                "currency": currency
            },
            "confirmation": {
                "type": "redirect",
                "return_url": return_url
            },
            "capture": True,
            "description": description
        }
    )
    return payment
