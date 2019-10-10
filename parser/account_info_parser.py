import lxml.html as html
from .base_parser import Parser
from urls.mainpageurl import MainPageUrl


class AccountInfo(Parser, MainPageUrl):

    def parse_info(self):
        page = html.fromstring(self._homepage)

        top_p = page.xpath('.//div[@class="header_top_item"]//span/text()')
        account_id, account_lvl, account_hnr, account_exp = map(lambda x: int(x.replace('.', '')), top_p)

        account_credits = page.xpath('.//div[@id="header_credits"]/text()')[0].strip().replace('.', '')
        account_uridium = page.xpath('.//a[@id="header_uri"]/text()')[0].strip().replace('.', '')

        self._data = {
            'id': account_id,
            'lvl': account_lvl,
            'hnr': account_hnr,
            'exp': account_exp,
            'credits': int(account_credits),
            'URI': int(account_uridium)
        }


def get_account_info(auth):
    return AccountInfo(auth)
