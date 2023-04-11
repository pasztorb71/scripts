import json

import requests
from requests.auth import HTTPBasicAuth

import utils


class Ticket:
    def __init__(self, ticket):
        self.name = ticket
        user_pass = utils.get_login_from_file()
        url = 'https://jira.icellmobilsoft.hu/rest/api/2/issue/'+ticket
        page = requests.get(url, auth=HTTPBasicAuth(user_pass[0], user_pass[1]))
        self.content = json.loads(str(page.content, 'utf-8'))

    def get_version(self):
        try:
            raw = self.content['fields']['fixVersions'][-1]['name'].replace('MLFF ','')
        except:
            return '0.07.0'
        #ver = raw.split()[1]
        tmp = raw.split('.')
        tmp[1] = tmp[1].rjust(2, '0')
        if len(tmp) == 3:
            return '.'.join(tmp)
        return '.'.join(tmp)+'.0'

    def get_title(self):
        return((self.content['fields']['summary']).replace(' ','_').replace('[','').replace(']',''))
