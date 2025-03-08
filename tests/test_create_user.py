import pytest
from generators.create_user_generator import CreateUser
from helpers.create_user import create_new_user


class TestCreateUser:

    def setup_method(self):
        self.data = CreateUser().add()

    def test_create_new_user(self):
        response = create_new_user(self.data)

        assert response.status_code == 200
        assert response.json()['user']['email'] == self.data['email']
        assert response.json()['user']['name'] == self.data['name']

    def test_create_already_registered_user(self):
        create_new_user(self.data)
        response = create_new_user(self.data)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @pytest.mark.parametrize('data', [CreateUser().set_password('').add(),
                                      CreateUser().set_email('').add(),
                                      CreateUser().set_name('').add()])
    def test_create_user_without_password_field(self, data):
        response = create_new_user(data)

        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
