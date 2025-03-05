import random
import string


def random_email(domain="gmail.com", length=10):
    username = f'{"".join(random.choices(string.ascii_letters + string.digits, k=length))}'
    return f"{username}@{domain}"


def random_password(length=10):
    return f'{"".join(random.choices(string.ascii_letters + string.digits, k=length))}'

def random_name(length=8):
    return f'{"".join(random.choices(string.ascii_letters + string.digits, k=length))}'
