import pytest
from generators.create_user_generator import CreateUser
from logic.user_service import create_new_user, delete_user, login_user
from helpers.utils import random_email, random_password, random_name


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


@pytest.fixture
def login_registered_user(create_new_user_fixture):
    data_for_login = {
        'email': create_new_user_fixture['email'],
        'password': create_new_user_fixture['password']}
    response = login_user(data_for_login)
    yield response.json()
