import asyncio

import stripe


async def check_payment_stripe(_id: str):
    while True:
        payment = await stripe.checkout.Session.retrieve_async(id=_id)
        if payment.status == 'complete':
            print(f'{payment.id}, {payment.amount_total} completed!')
        if payment.status != 'open':
            break
        await asyncio.sleep(delay=60)


async def create_payment_stripe(
        price: str, currency: str, success_url: str, cancel_url: str
) -> stripe.checkout.Session:
    """returns a payment"""
    stripe.api_key = 'sk_test_51PUU0CJ9MetCi25fM4NUOeKk6rjajvevF0Q7KR5QGVayguvWpGOFajhzve1iKGhF57Dz640siQpjev133XT1PQid00jORsny05'
    session = await stripe.checkout.Session.create_async(
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
    return session
