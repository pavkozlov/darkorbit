import lxml.html as html
from .base_parser import Parser
from urls.skylaburl import SkylabUrl

resources1 = ['base_level', 'solar_level', 'storage_level', 'transport_level', 'xeno_level', 'prometium_level',
              'endurium_level', 'terbium_level', 'prometid_level', 'duranium_level', 'promerium_level', 'seprom_level']
resources2 = ['prometium_count', 'endurium_count', 'terbium_count', 'prometid_count',
              'duranium_count', 'xeno_count', 'promerium_count', 'seprom_count']


class SkyLabInfo(Parser, SkylabUrl):

    def parse_info(self):
        page = html.fromstring(self._homepage)
        levels = page.xpath('.//div[@class="level skylab_font_level"]/text()')
        resource_levels = {a: int(b) for a, b in zip(resources1, levels)}

        resource_count = page.xpath('.//div[@class="view_generally"]//div//text()')
        resource_count = list(filter(lambda x: x != '', [i.strip() for i in resource_count]))[1::3]
        resource_count = {a: int(b.replace(',', '')) for a, b in zip(resources2, resource_count)}

        result = resource_levels.copy()
        result.update(resource_count)
        self._data = result


def get_skylab_info(auth):
    return SkyLabInfo(auth)
