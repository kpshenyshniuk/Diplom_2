import requests
from data.data import get_user_orders_link, ingredients
from helpers.create_order import create_order


class TestGetUserOrders:

    def test_get_user_orders(self, login_registered_user):
        token = login_registered_user['accessToken']
        create_order(token, ingredients)
        headers = {"Authorization": f"{token}"}
        response = requests.get(get_user_orders_link, headers=headers)

        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)
        assert response.json()['orders'][0]['ingredients'] == ingredients['ingredients']

    def test_get_user_orders_without_token(self, login_registered_user):
        token = login_registered_user['accessToken']
        create_order(token, ingredients)
        headers = {"Authorization": f""}
        response = requests.get(get_user_orders_link, headers=headers)
        print(response.json())
        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'
