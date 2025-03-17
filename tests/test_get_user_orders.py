import allure
import requests
from data.data import get_user_orders_link, correct_ingredients, authorised_required
from logic.order_service import create_order


class TestGetUserOrders:

    @allure.title("Тест получения всех заказов пользователя")
    def test_get_user_orders(self, login_registered_user):
        token = login_registered_user['accessToken']
        create_order(token, correct_ingredients)
        headers = {"Authorization": f"{token}"}
        response = requests.get(get_user_orders_link, headers=headers)

        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)
        assert response.json()['orders'][0]['ingredients'] == correct_ingredients['ingredients']

    @allure.title("Тест получения всех заказов без авторизации")
    def test_get_user_orders_without_token(self, login_registered_user):
        token = login_registered_user['accessToken']
        create_order(token, correct_ingredients)
        headers = {"Authorization": f""}
        response = requests.get(get_user_orders_link, headers=headers)

        assert response.status_code == 401
        assert response.json()['message'] == authorised_required
