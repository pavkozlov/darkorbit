import requests
from bs4 import BeautifulSoup
import re
import config


class DarkorbitAuth:
    def __init__(self):
        self.session = requests.session()
        self.security_token = self.get_security_token()
        self.server = None
        self.info = None
        self.skylab = None
        self.do_url = None
        self.skylab_lvls = None

    def get_security_token(self):
        r = requests.get('https://www.darkorbit.ru/')
        soup = BeautifulSoup(r.text, 'lxml')
        token = soup.find('div', class_="bgcdw_login_container_form").find('form').get('action')
        return token

    def auth(self):
        data = {'username': config.AUTH['login'], 'password': config.AUTH['password']}
        auth = self.session.post(self.security_token, data=data)
        server = re.search('https://(.*).darkorbit.com/', auth.url)
        assert server, 'Не правильный логин/пароль'
        return server.group(1)

    def get_info(self):
        r = self.session.get(self.do_url + 'internalStart').text
        soup = BeautifulSoup(r, 'lxml')
        top_panel = soup.findAll('div', class_='header_top_item')
        top_panel = list(map(config.clean_data, (i.text for i in top_panel)))
        credits_count = config.clean_data(soup.find('div', id='header_credits').text)
        uridium = config.clean_data(soup.find('a', id='header_uri').text)
        info = {'id': top_panel[0], 'level': top_panel[1], 'honor': top_panel[2],
                'exp': top_panel[3], 'credits': credits_count, 'uridium': uridium}
        return info

    def get_skylab(self):
        r = self.session.get(self.do_url + 'internalSkylab').text
        soup = BeautifulSoup(r, 'lxml')
        resourses = soup.findAll('div', class_='view_generally')
        result = dict()
        for resource in resourses:
            res = resource.find('div').text
            res = res.strip().split()
            result[res[0][:len(res[0]) - 1]] = config.clean_data(res[1])
        return result

    def get_skylab_levels(self):
        r = self.session.get(self.do_url + 'internalSkylab').text
        soup = BeautifulSoup(r, 'lxml')
        res = soup.find('table', class_='module_infobox_baseModule').findAll('tr')
        result = dict()
        for i in res:
            r = i.findAll('td')
            result[r[0].text] = config.clean_data(r[2].text)
        return result

    def authorize(self):
        self.server = self.auth()
        self.do_url = config.return_url(self.server)
        self.info = self.get_info()
        self.skylab = self.get_skylab()
        self.skylab_lvls = self.get_skylab_levels()
