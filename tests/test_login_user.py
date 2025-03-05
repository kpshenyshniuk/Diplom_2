import pytest
from generators.create_user_generator import CreateUser
from helpers.create_user import create_new_user
from helpers.login import login_user


class TestCreateUser:

    def setup_class(self):
        self.data_for_register = CreateUser().add()
        self.response_create_user = create_new_user(self.data_for_register)
        self.data_for_login = {
            'email': self.data_for_register['email'],
            'password': self.data_for_register['password']
        }

    def test_login_registered_user(self):
        response = login_user(self.data_for_login)
        print(response.json())
        assert response.status_code == 200





    def test_create_already_registered_user(self):
        create_new_user(self.data)
        response = create_new_user(self.data)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @pytest.mark.parametrize('data', [CreateUser().set_password('').add(),
                                       CreateUser().set_email('').add(),
                                       CreateUser().set_name('').add()])
    def test_create_user_without_password_field(self,data):
        response = create_new_user(data)

        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
        print(response.json())
