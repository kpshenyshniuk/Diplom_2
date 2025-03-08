import requests
from data.data import create_order_link


def create_order(token, ingredients):
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    response = requests.post(create_order_link, headers=headers, json=ingredients)
    return response
