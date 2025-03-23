import random
import string
import allure


@allure.step("Создаем рандомный email, возвращаем данный email")
def random_email(domain="gmail.com", length=10):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"


@allure.step("Создаем рандомный password, возвращаем данный password")
def random_password(length=10):
    return f'{"".join(random.choices(string.ascii_letters + string.digits, k=length))}'


@allure.step("Создаем рандомный name, возвращаем данный name")
def random_name(length=8):
    return f'{"".join(random.choices(string.ascii_letters + string.digits, k=length))}'
