import allure
import requests
from data.data import create_new_user_link, delete_user_link, login_link, get_and_update_user_profile_link


@allure.step("Создание нового пользователя, возвращаем response")
def create_new_user(data):
    response = requests.post(create_new_user_link, json=data)
    return response

@allure.step("Удаление пользователя, возвращаем response")
def delete_user(token):
    headers = {"Authorization": token}
    response = requests.delete(delete_user_link, headers=headers)
    return response

@allure.step("Авторизация пользователя, возвращаем response")
def login_user(data):
    response = requests.post(login_link, json=data)
    return response


@allure.step("Получаем данные о пользователе пользователя, возвращаем response")
def get_user_profile(token):
    response = requests.get(get_and_update_user_profile_link, auth=token)
    return response

@allure.step("Обновляем данные о пользователе пользователя, возвращаем response")
def update_user_profile(token, data):
    response = requests.patch(get_and_update_user_profile_link, headers={"Authorization": token}, json=data)
    return response.json()
