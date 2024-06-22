import uuid
import requests

import stripe

from settings.base import SHOP_ID, SHOP_SECRET_KEY


def create_payment_youkassa(price: str, currency: str, return_url, description: str):
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


def create_payment_stripe(price: str, currency: str, success_url: str, cancel_url: str) -> str:
    """returns a payment utl"""
    stripe.api_key = 'sk_test_51PUU0CJ9MetCi25fM4NUOeKk6rjajvevF0Q7KR5QGVayguvWpGOFajhzve1iKGhF57Dz640siQpjev133XT1PQid00jORsny05'
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': currency,
                'product_data': {
                    'name': 'Order on the olives shop website',
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )

    return session.url
