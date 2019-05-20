from bs4 import BeautifulSoup
import config
import re
import time


class SkyLab:
    def __init__(self, auth):
        self.session = auth.session
        self.do_url = auth.do_url
        self.info = auth.info
        self.skylab = auth.skylab

        self.ready_to_upd = self.upd_skylab()

    def upd_skylab(self):
        r = self.session.get(self.do_url + 'internalSkylab').text
        soup = BeautifulSoup(r, 'lxml')
        res = soup.findAll('table', class_='module_infobox_upgrade')
        ready_to_upd = list()
        for i in res:
            trs = i.findAll('tr')
            resourses = {
                trs[6].find('td', class_='firstRow').text: config.clean_data(trs[6].findAll('td')[3].text),
                trs[7].find('td', class_='firstRow').text: config.clean_data(trs[7].findAll('td')[3].text),
                trs[8].find('td', class_='firstRow').text: config.clean_data(trs[8].findAll('td')[3].text)
            }
            url = i.findAll('tr')[10].findAll('a')[1].get('href')
            url = re.search('action=(.*)', url).group(1)
            module = {
                'name': re.search('construction=(.*)&', url).group(1),
                'credits': config.clean_data(trs[4].findAll('td')[1].text),
                'time': trs[5].findAll('td')[3].text.strip(),
                'resourses': resourses,
                'url': self.do_url + url,
            }
            ready_to_upd.append(module)
        return ready_to_upd

    def update(self):
        for item in self.ready_to_upd:
            self.session.get(item['url'])
            time.sleep(2)
