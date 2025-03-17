import allure

from data.data import incorrect_email_password
from generators.create_user_generator import CreateUser
from logic.user_service import login_user


class TestLoginUsers:

    @allure.title("Тест авторизации зарегистрированного пользователя")
    def test_login_registered_user(self, create_new_user_fixture):
        data_for_login = {
            'email': create_new_user_fixture['email'],
            'password': create_new_user_fixture['password']}
        response = login_user(data_for_login)

        assert response.status_code == 200
        assert response.json().get('accessToken')
        assert response.json().get('refreshToken')

    @allure.title("Тест авторизации не зарегистрированного пользователя")
    def test_login_not_registered_user(self):
        new_data = CreateUser().add()
        response = login_user(new_data)

        assert response.status_code == 401
        assert response.json()['message'] == incorrect_email_password
