import json
import re

import requests
from bs4 import BeautifulSoup

from requests.auth import HTTPBasicAuth

from utils import get_login_from_file


class Confluence:
    def get_table_from_url(self, url):
        token = 'ATATT3xFfGF0syQvBtTArocAo21QTU-oCYHmEkaABGDXWASB4U-cGvjnSd8iEYC8icEQz-h-Qwy9Al5kwsVenQPj0jC8DJFS6S6eQE1oE4cufXYGQo2uQQA5FR4ZAKKNM_73g4X9XK7tIX3Ulam-xfHWHe8yJmVKK-zcMrrx3VgtbbYwJIUxZZg=0BBDC6E7'
        page = requests.get(url, auth=HTTPBasicAuth('bertalan.pasztor@icellmobilsoft.hu', token))
        cont = page.text
        page_id = url.split('/pages/')[1].split('/',1)[0]
        url = 'https://icellmobilsoft-int.atlassian.net/wiki/rest/api/content/' + str(page_id) + '?expand=body.storage'
        self.page = requests.get(url, auth=HTTPBasicAuth('bertalan.pasztor@icellmobilsoft.hu', token))
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
