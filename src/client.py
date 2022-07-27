from atlassian import Bamboo
from data import Plan
import json

from formatter import TableFormatter, JsonFormatter


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

        if output == 'json':
            formatter = JsonFormatter()
        else:
            formatter = TableFormatter(bamboo_base_url=self.bamboo.url)

        formatter.format(plans)
