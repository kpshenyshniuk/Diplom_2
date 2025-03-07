import pytest
from generators.create_user_generator import CreateUser
from helpers.create_user import create_new_user
from helpers.login import login_user


class TestCreateUser:

    def test_login_registered_user(self, create_new_user_fixture):
        data_for_login = {
            'email': create_new_user_fixture['email'],
            'password': create_new_user_fixture['password']}
        response = login_user(data_for_login)
        print(response.json()['accessToken'])
        assert response.status_code == 200
        assert response.json().get('accessToken')
        assert response.json().get('refreshToken')


    def test_login_not_registered_user(self):
        new_data = CreateUser().add()
        response = login_user(new_data)

        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'
