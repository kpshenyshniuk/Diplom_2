import requests
from data.data import create_order_link, get_user_orders_link


def create_order(token, ingredients):
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    response = requests.post(create_order_link, headers=headers, json=ingredients)
    return response


def get_user_orders(token):
    response = requests.get(f'{get_user_orders_link} + {token}')
    return response
