import requests
import re
from bs4 import BeautifulSoup


class DarkorbitAuth:
    def __init__(self, login, password):
        self.login_name = login
        self.password = password
        self.session = requests.Session()
        self.auth = self.login()
        self.info = self.get_info()

    def login(self):
        main_page = self.session.get("https://www.darkorbit.ru/")
        token = re.findall('Bigpoint\?authUser=22&amp;token=(.*)"', main_page.text)[0]
        data = {'username': self.login_name, 'password': self.password}
        auth = self.session.post(f'https://sas.bpsecure.com/Sas/Authentication/Bigpoint?authUser=22&token={token}',
                                 data=data)
        if re.search('https:\/\/(.*)\.darkorbit\.com\/indexInternal\.es\?action=internalStart(.*)?', auth.url):
            return auth
        else:
            raise Exception('Не верно введён логин и/или пароль')

    def get_info(self):
        soup = BeautifulSoup(self.auth.text, features='html.parser')
        sid = soup.find_all('script', language="javascript")[1]
        info = {
            'id': soup.find('div', id="header_top_id").span.text,
            'sid': re.search("dosid=(.*)'\);", str(sid)).group(1),
            'server': re.search('\/\/(.*)\.darkorbit\.com\/indexInternal\.es', self.auth.url).group(1),
            'level': soup.find('div', id="header_top_level").span.text,
            'exp': soup.find('div', id="header_top_exp").span.text,
            'honor': soup.find('div', id="header_top_hnr").span.text,
            'uri_count': soup.find('a', id='header_uri').text.strip().strip(),
            'credits_count': soup.find('div', id='header_credits').text.strip()
        }
        return info
