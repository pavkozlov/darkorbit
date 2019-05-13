from Darkorbit import auth
from config import AUTH


def run():
    text = auth.DarkorbitAuth(AUTH['login'], AUTH['password'])
    for item in text.info:
        print(f'{item} : {text.info[item]}')
