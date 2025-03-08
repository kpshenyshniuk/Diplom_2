import requests
from data.data import get_user_orders_link


def get_user_orders(token):
    response = requests.get(f'{get_user_orders_link} + {token}')
    return response
