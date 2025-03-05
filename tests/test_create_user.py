import requests

from data.links import create_new_user_link
from generators.create_user_generator import CreateUser


class TestCreateUser:

    def setup_method(self):
        self.data = CreateUser()  # Создаём объект


    def test_cteate_new_user(self):
        requests.post(create_new_user_link, json=self.data)