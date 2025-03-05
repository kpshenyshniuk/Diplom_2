import requests
from data.links import create_new_user_link


def create_new_user(data):
    response = requests.post(create_new_user_link, json=data)
    return response
