import allure

from helpers.utils import random_password, random_name, random_email


class CreateUser:


    def __init__(self):

        self.data = {
            'email': random_email(),
            'password': random_password(),
            'name': random_name()
        }

    @allure.step("устанавливаем передаваемый email в data")
    def set_email(self, email):
        self.data['email'] = email
        return self

    @allure.step("устанавливаем передаваемый password в data")
    def set_password(self, password):
        self.data['password'] = password
        return self

    @allure.step("устанавливаем передаваемый name в data")
    def set_name(self, name):
        self.data['name'] = name
        return self

    @allure.step("получаем email из data")
    def get_email(self):
        return {'email': self.data['email']}

    @allure.step("получаем password из data")
    def get_password(self):
        return {'password': self.data['password']}

    @allure.step("получаем name из data")
    def get_name(self):
        return {'name': self.data['name']}

    @allure.step("возвращает data")
    def add(self):
        return self.data
