import requests
from data.data import create_order_link


def create_order(token, ingredients):
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    response = requests.post('https://stellarburgers.nomoreparties.site/api/orders', headers=headers, json=ingredients)
    return response
