import requests
from data.data import create_new_user_link, get_user_orders_link


def get_user_orders(token):
    response = requests.get(f'{get_user_orders_link} + {token}')
    return response
