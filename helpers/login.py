import requests

from data.links import login_link


def login_user(data):
    response = requests.post(login_link, json=data)
    return response
