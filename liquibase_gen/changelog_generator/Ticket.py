import json

import requests
from requests.auth import HTTPBasicAuth

from utils import get_login_from_file


class Ticket:
    def __init__(self, ticket):
        self.name = ticket
        user_pass = get_login_from_file()
        url = 'https://jira.icellmobilsoft.hu/rest/api/2/issue/'+ticket
        page = requests.get(url, auth=HTTPBasicAuth(user_pass[0], user_pass[1]))
        self.content = json.loads(str(page.content, 'utf-8'))

    def get_version(self):
        raw = self.content['fields']['fixVersions'][0]['name']
        ver = raw.split()[1]
        tmp = ver.split('.')
        tmp[1] = tmp[1].rjust(2, '0')
        return '.'.join(tmp)+'.0'
