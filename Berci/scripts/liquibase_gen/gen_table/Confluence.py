import json
import re

import requests

from requests.auth import HTTPBasicAuth

from utils import get_login_from_file


class Confluence:
    def get_table_from_url(self, url):
        user_pass = get_login_from_file()
        page = requests.get(url, auth=HTTPBasicAuth(user_pass[0], user_pass[1]))
        cont = page.text
        page_id = re.match('.*<meta name="ajs-page-id" content="([0-9]*)">', cont, flags=re.DOTALL).group(1)
        url = 'https://confluence.icellmobilsoft.hu/rest/api/content/' + str(page_id) + '?expand=body.storage'
        self.page = requests.get(url, auth=HTTPBasicAuth('bertalan.pasztor', 'Tcg6276tcg'))
        return page.text.replace('\\"','\"')

    def get_table_comment(self):
        _dict = json.loads(self.page.text)
        f = _dict['body']['storage']['value']
        a = re.match('.*<p( style="")?>(.*)</p>.*<table.*(?:<table).*',f)
        #g1 = a.group(1)
        #g2 = a.group(2)
        return a.group(2) if a else ''
