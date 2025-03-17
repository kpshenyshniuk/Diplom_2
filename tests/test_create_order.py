from data.data import correct_ingredients, error_ingredient_id, not_existed_ingredient
from logic.order_service import create_order
import allure

class TestCreateOrder:

    @allure.title("Создание заказа авторизированным пользователем")
    def test_create_order_with_authentification(self, login_registered_user):
        token = login_registered_user['accessToken']
        response = create_order(token, correct_ingredients)

        assert response.json()['success'] == True
        assert response.json()['order']['ingredients'][0]['_id'] == correct_ingredients['ingredients'][0]
        assert response.json()['order']['owner']['email'] == login_registered_user['user']['email']

    @allure.title("Создание заказа не авторизированным пользователем")
    def test_create_order_without_authentification(self):
        token = ''
        response = create_order(token, correct_ingredients)

        assert response.json()['success'] == False

    @allure.title("Создание заказа без ингридиентов")
    def test_create_order_without_ingredients(self, login_registered_user):
        token = login_registered_user['accessToken']
        ingredients = {"ingredients": ''}
        response = create_order(token, ingredients)

        assert response.json()['success'] == False
        assert response.json()['message'] == error_ingredient_id

    @allure.title("Создание заказа с некоректными ингридиентами")
    def test_create_order_with_incorrect_ingredients(self, login_registered_user):
        token = login_registered_user['accessToken']
        response = create_order(token, not_existed_ingredient)

        assert response.status_code == 500
