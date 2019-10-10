from .baseurl import BaseUrl


class MainPageUrl(BaseUrl):
    def get_url(self, server):
        return f'https://{server}.darkorbit.com/indexInternal.es?action=internalStart'
