import requests
from data.data import get_and_update_user_profile_link


def get_user_profile(token):
    response = requests.get(get_and_update_user_profile_link, auth=token)
    return response


def update_user_profile(token, data):
    response = requests.patch(get_and_update_user_profile_link, headers={"Authorization": token}, json=data)
    return response.json()
