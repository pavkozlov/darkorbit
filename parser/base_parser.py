from urls.baseurl import BaseUrl


class Parser(BaseUrl):
    def __init__(self, auth):
        self._data = None
        self.session = auth.get_session()
        self.server = auth.get_server()
        self._homepage = self.session.get(self.get_url(self.server)).text
        self.parse_info()

    def parse_info(self):
        pass

    def get_info(self):
        return self._data
