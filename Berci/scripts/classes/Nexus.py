import json

import requests
from requests.auth import HTTPBasicAuth

from classes.Repository import Repository
from utils.utils_sec import get_nexus_login_from_file


class Nexus():
    def __init__(self):
        login = get_nexus_login_from_file()
        self.user = login[0]
        self.passw = login[1]
        self.url = "https://hubphq-mlff-nexus-p002.icellmobilsoft.hu/service/rest/v1/search?repository=dockerhub-mlff&name=liquibase/"

    def get_repo_versions_from_items(self, items):
        out = {}
        for item in items:
            item_name = item['name'].replace('liquibase/','')
            if item_name in out.keys():
                out[item_name].append(item['version'])
            else:
                out[item_name] = []
        return out

    def get_mlff_repositories(self, repo='mlff-*'):
        items = []
        continuationtoken = None
        base_url = self.url + repo
        while True:
            if continuationtoken:
                url = base_url + f'&continuationToken={continuationtoken}'
            else:
                url = base_url
            page = requests.get(url, auth=HTTPBasicAuth(self.user, self.passw))
            content = json.loads(page.text)
            items += content['items']
            continuationtoken = content['continuationToken']
            if not continuationtoken:
                break
        return items

    def get_last_image_ver_of_repo(self, repo_name):
        items = self.get_mlff_repositories(repo_name)
        versions = self.get_repo_versions_from_items(items)
        return versions[repo_name][-1]

if __name__ == '__main__':
    n = Nexus()
    repo_name = Repository('detection-alert-pos').name
    #items = n.get_mlff_repositories(repo_name)
    #items = n.get_mlff_repositories()
    #versions = n.get_repo_versions_from_items(items)
    a = n.get_last_image_ver_of_repo(repo_name)
    print(a)