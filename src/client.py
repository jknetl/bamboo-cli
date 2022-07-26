from atlassian import Bamboo
from tabulate import tabulate
from data import Plan
import json


class BambooClient:

    def __init__(self, server: str, username: str, password: str, ssl_verify=True):
        self.bamboo = Bamboo(url=server, username=username, password=password, verify_ssl=ssl_verify)

    def get_plan(self, key: str):
        plan = self.bamboo.get_plan(key)
        json_object = json.dumps(plan, indent=4)
        print(json_object)

    def search_plan(self, name, project, output):
        result = self.bamboo.search_plan(name)
        plans = [Plan(p['searchEntity']) for p in result['searchResults']]

        if (output == 'json'):
            json_object = json.dumps(result, indent=4)
            print(json_object)
        else:
            table = [p.as_readable_list() for p in plans]
            print(tabulate(table, headers=["Key", "Name", "Project"]))
