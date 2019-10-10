import requests
import lxml.html as html
import re


class DarkOrbitAuth:
    def __init__(self, username, password, session):
        self._username, self._password, self._session = username, password, session

    def get_url(self):
        homepage = self._session.get('https://www.darkorbit.ru/').text
        return html.fromstring(homepage).xpath('.//div[@class="bgcdw_login_container_form"]/form/@action')[0]

    def auth(self, auth_url):
        data = {'username': self._username, 'password': self._password}
        authenticate = self._session.post(auth_url, data=data)
        return re.search('https://(.*).darkorbit.com/', authenticate.url).group(1)

    def get_server(self):
        return self._server

    def get_session(self):
        return self._session


def auth(username, password):
    session = requests.session()
    au_session = DarkOrbitAuth(username, password, session)
    au_session._server = au_session.auth(au_session.get_url())
    return au_session
