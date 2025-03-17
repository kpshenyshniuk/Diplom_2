import requests
from data.data import create_new_user_link, delete_user_link, login_link, get_and_update_user_profile_link


def create_new_user(data):
    response = requests.post(create_new_user_link, json=data)
    return response


def delete_user(token):
    headers = {"Authorization": token}
    response = requests.delete(delete_user_link, headers=headers)
    return response


def login_user(data):
    response = requests.post(login_link, json=data)
    return response


def get_user_profile(token):
    response = requests.get(get_and_update_user_profile_link, auth=token)
    return response


def update_user_profile(token, data):
    response = requests.patch(get_and_update_user_profile_link, headers={"Authorization": token}, json=data)
    return response.json()
