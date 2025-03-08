import pytest
from generators.create_user_generator import CreateUser
from helpers.create_user import create_new_user
from helpers.login import login_user


@pytest.fixture
def create_new_user_fixture():
    data_for_register = CreateUser().add()
    create_new_user(data_for_register)
    yield data_for_register
    """
        Потом добавить бан узера
        """


@pytest.fixture
def login_registered_user(create_new_user_fixture):
    data_for_login = {
        'email': create_new_user_fixture['email'],
        'password': create_new_user_fixture['password']}
    response = login_user(data_for_login)
    yield response.json()
