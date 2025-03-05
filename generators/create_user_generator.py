from helpers.global_helpers import random_password, random_name, random_email



class CreateUser:


    def __init__(self):

        self.data = {
            'email': random_email(),
            'password': random_password(),
            'name': random_name()
        }

    def set_email(self, email):
        self.data['email'] = email
        return self

    def set_password(self, password):
        self.data['password'] = password
        return self

    def set_name(self, name):
        self.data['name'] = name
        return self

    def get_email(self):
        return {'email': self.data['email']}

    def get_password(self):
        return {'password': self.data['password']}

    def get_name(self):
        return {'name': self.data['name']}
