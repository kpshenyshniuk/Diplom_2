import allure
import pytest
from logic.user_service import create_new_user, delete_user, login_user
from helpers.utils import random_email, random_password, random_name


@allure.step("Фикстура создание нового пользователя")
@pytest.fixture
def create_new_user_fixture():
    """Фикстура для создания нового пользователя и его удаления после теста."""
    data_for_register = {
        'email': random_email(),
        'password': random_password(),
        'name': random_name()
    }
    response = create_new_user(data_for_register)
    response_json = response.json()
    access_token = response_json.get('accessToken')

    yield data_for_register
    delete_user(access_token)


@allure.step("Фикстура авторизации нового пользователя")
@pytest.fixture
def login_registered_user(create_new_user_fixture):
    data_for_login = {
        'email': create_new_user_fixture['email'],
        'password': create_new_user_fixture['password']}
    response = login_user(data_for_login)
    yield response.json()


@allure.step("Фикстура создания даных для нового пользователя")
@pytest.fixture
def data_for_user():
    data = {
        'email': random_email(),
        'password': random_password(),
        'name': random_name()
    }
    yield data
