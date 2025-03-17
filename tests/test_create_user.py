import allure
import pytest

from data.data import User_already_exist, required_field
from generators.create_user_generator import CreateUser
from logic.user_service import create_new_user


class TestCreateUsers:


    @allure.title("Создание нового пользователя")
    def test_create_new_user(self):
        response = create_new_user(self.data)

        assert response.status_code == 200
        assert response.json()['user']['email'] == self.data['email']
        assert response.json()['user']['name'] == self.data['name']

    @allure.title("Создание пользователя с уже существующими кредами")
    def test_create_already_registered_user(self):
        create_new_user(self.data)
        response = create_new_user(self.data)

        assert response.status_code == 403
        assert response.json()['message'] == User_already_exist

    @allure.title("Создание пользователя без поля pawword")
    @pytest.mark.parametrize('data', [CreateUser().set_password('').add(),
                                      CreateUser().set_email('').add(),
                                      CreateUser().set_name('').add()])
    def test_create_user_without_password_field(self, data):
        response = create_new_user(data)

        assert response.status_code == 403
        assert response.json()['message'] == required_field
