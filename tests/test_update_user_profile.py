from helpers.global_helpers import random_email, random_name
from helpers.update_user_profile import update_user_profile


class TestUpdateUserProfile:

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

    def test_update_user_profile_without_authentification(self):
        token = ''
        new_data = {
            'email': random_email(),
            'name': random_name()
        }
        response = update_user_profile(token, new_data)

        assert response['success'] == False
        assert response['message'] == 'You should be authorised'
