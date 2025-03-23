import allure
import requests
from data.data import create_order_link, get_user_orders_link


@allure.step("Создаем заказ авторизированный пользователем, возвращаем response")
def create_order(token, ingredients):
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    response = requests.post(create_order_link, headers=headers, json=ingredients)
    return response

@allure.step("Получаем все заказы пользователя, возвращаем response")
def get_user_orders(token):
    response = requests.get(f'{get_user_orders_link} + {token}')
    return response
