import json
import re

import requests

from requests.auth import HTTPBasicAuth


class Confluence:
    def get_table_from_url(self, url):
        page = requests.get(url, auth=HTTPBasicAuth('bertalan.pasztor', 'Tcg6276tcg'))
        cont = page.text
        page_id = re.match('.*<meta name="ajs-page-id" content="([0-9]*)">', cont, flags=re.DOTALL).group(1)
        url = 'https://confluence.icellmobilsoft.hu/rest/api/content/' + str(page_id) + '?expand=body.storage'
        self.page = requests.get(url, auth=HTTPBasicAuth('bertalan.pasztor', 'Tcg6276tcg'))
        return page.text.replace('\\"','\"')

    def get_table_comment(self):
        _dict = json.loads(self.page.text)
        f = _dict['body']['storage']['value']
        a = re.match('.*<p( style="")?>(.*)</p>.*<table',f)
        return a.group(2)
