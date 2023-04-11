import json
import re

import requests
from bs4 import BeautifulSoup

from requests.auth import HTTPBasicAuth

from utils import get_login_from_file


class Confluence:
    def get_table_from_url(self, url):
        page = requests.get(url, auth=HTTPBasicAuth('bertalan.pasztor@icellmobilsoft.hu', 'ATATT3xFfGF0A1oSri6POQVqhVIvquW92TD7gBUh2jkdEkLi6AlOSMCbN1I73j6sdD8taiV0V9DwO3aSNCLvgX'))
        cont = page.text
        page_id = url.split('/pages/')[1].split('/',1)[0]
        url = 'https://icellmobilsoft-int.atlassian.net/wiki/rest/api/content/' + str(page_id) + '?expand=body.storage'
        self.page = requests.get(url, auth=HTTPBasicAuth('bertalan.pasztor@icellmobilsoft.hu', 'ATATT3xFfGF0A1oSri6POQVqhVIvquW92TD7gBUh2jkdEkLi6AlOSMCbN1I73j6sdD8taiV0V9DwO3aSNCLvgX-lpLQeZ4Doo0DnYwAF89OQrSvjWapstluT7QP3xwFDRd88x8vtNwXsJeeVIqbS9uJYrmG3_je6AuTT-YOB62aWKkKbb2B3pRs=F591E37B'))
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
