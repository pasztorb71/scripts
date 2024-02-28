import json

import requests
from requests.auth import HTTPBasicAuth

from Repository import Repository
from utils.utils_sec import get_nexus_login_from_file


class Nexus():
    def __init__(self):
        login = get_nexus_login_from_file()
        self.user = login[0]
        self.passw = login[1]
        self.url = "https://hubphq-mlff-nexus-p002.icellmobilsoft.hu/service/rest/v1/search?repository=dockerhub-mlff&name=liquibase/"

    def get_repo_versions(self, repo):
        url = self.url + repo
        page = requests.get(url, auth=HTTPBasicAuth(self.user, self.passw))
        return [x['version'] for x in json.loads(page.text)['items']]

    def get_mlff_repo_names(self):

if __name__ == '__main__':
    n = Nexus()
    page = n.get_repo_versions(Repository('detection-pos').name)
    pass