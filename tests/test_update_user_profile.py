import allure

from data.data import authorised_required
from helpers.utils import random_email, random_name
from logic.user_service import update_user_profile


class TestUpdateUserProfile:

    @allure.title("Тест обновление профиля авторизированного пользователя")
    def test_update_user_profile_with_authentification(self, login_registered_user):
        token = login_registered_user['accessToken']
        new_data = {
            'email': random_email(),
            'name': random_name()
        }
        response = update_user_profile(token, new_data)

        assert response['success'] == True
        assert response['user']['email'] == new_data['email']
        assert response['user']['name'] == new_data['name']

    @allure.title("Тест обновление профиля не авторизированного пользователя")
    def test_update_user_profile_without_authentification(self):
        token = ''
        new_data = {
            'email': random_email(),
            'name': random_name()
        }
        response = update_user_profile(token, new_data)

        assert response['success'] == False
        assert response['message'] == authorised_required
