from data.data import ingredients
from helpers.create_order import create_order


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
