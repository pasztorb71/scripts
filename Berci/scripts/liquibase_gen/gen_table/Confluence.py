import json
import re

import requests
from bs4 import BeautifulSoup

from requests.auth import HTTPBasicAuth

import utils
from utils.utils import get_atlassian_login_from_file


class Confluence:
    def get_table_from_url(self, url):
        user_pass = get_atlassian_login_from_file()
        page = requests.get(url, auth=HTTPBasicAuth(user_pass[0], user_pass[1]))
        cont = page.text
        page_id = url.split('/pages/')[1].split('/',1)[0]
        baseurl = 'https://icellmobilsoft-int.atlassian.net'
        url = f'{baseurl}/wiki/rest/api/content/{str(page_id)}?expand=body.storage'
        self.page = requests.get(url, auth=HTTPBasicAuth(user_pass[0], user_pass[1]))
        return self.page.text.replace('\\"','\"')

    def get_table_comment(self):
        parsed_html = BeautifulSoup(self.page.text, features="lxml")
        txt = parsed_html.body.find('p').findNext("p").get_text()
        return txt
        _dict = json.loads(self.page.text)
        f = _dict['body']['storage']['value']
        a = re.match('.*<p( style="")?>(.*)</p>.*<table.*(?:<table).*',f)
        #g1 = a.group(1)
        #g2 = a.group(2)
        return a.group(2) if a else ''
