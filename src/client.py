from atlassian import Bamboo
from data import Plan
import json

from formatter import TableFormatter, JsonFormatter
from data import ResourceType


class BambooPlanClient:

    def __init__(self, server: str, username: str, password: str, ssl_verify=True):
        self.bamboo = Bamboo(url=server, username=username, password=password, verify_ssl=ssl_verify)

    def get(self, key: str):
        plan = self.bamboo.get_plan(key)
        json_object = json.dumps(plan, indent=4)
        print(json_object)

    def search(self, name, output):
        index = 0
        plans = []
        while True:
            result = self.bamboo.search_plans(name, start_index=index, max_results=500)
            plans += [Plan(p['searchEntity']) for p in result['searchResults']]
            index = result['start-index'] + result['max-result']
            if index == result['size']:
                break

        if output == 'json':
            formatter = JsonFormatter()
        else:
            formatter = TableFormatter(bamboo_base_url=self.bamboo.url)

        formatter.format(plans)

    def toggle_enabled(self, key: str, enabled: bool):
        if enabled:
            self.bamboo.enable_plan(key)
        else:
            self.bamboo.disable_plan(key)

    def delete(self, key: str):
        self.bamboo.delete_plan(key)


def create_bamboo_client(args):
    resource_type = ResourceType.from_str(args.resource_type)
    if resource_type == ResourceType.PLAN:
        return BambooPlanClient(args.server, args.user, args.password, ssl_verify=(not args.ssl_no_verify))
    elif resource_type == ResourceType.DEPLOYMENT:
        raise Exception("Working with deployments in not implement yet!")
