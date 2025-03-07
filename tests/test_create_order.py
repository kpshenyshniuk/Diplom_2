import pytest
import requests
from data.data import get_and_update_user_profile_link, create_order_link, ingredients
from generators.create_user_generator import CreateUser
from helpers.create_order import create_order
from helpers.create_user import create_new_user
from helpers.global_helpers import random_email, random_name
from helpers.login import login_user
from helpers.update_user_profile import update_user_profile


class TestCreateOrder:

    def test_create_order_with_authentification(self, login_registered_user):
        token = login_registered_user['accessToken']
        response = create_order(token, ingredients)

        assert response.json()['success'] == True
        assert response.json()['order']['ingredients'][0]['_id'] == ingredients['ingredients'][0]
        assert response.json()['order']['owner']['email'] == login_registered_user['user']['email']

    def test_create_order_without_authentification(self):
        token = ''
        response = create_order(token, ingredients)
        print(response.json())

        assert response.json()['success'] == False


    def test_create_order_without_ingredients(self, login_registered_user):
        token = login_registered_user['accessToken']
        ingredients = {"ingredients": ''}
        response = create_order(token, ingredients)

        assert response.json()['success'] == False
        assert response.json()['message'] == 'Ingredient ids must be provided'


    def test_create_order_with_incorrect_ingredients(self, login_registered_user):
        token = login_registered_user['accessToken']
        ingredients = {"ingredients": 'ksdfklsdfksdlfsdkf'}
        response = create_order(token, ingredients)

        assert response.status_code == 500
