from atlassian import Bamboo
from pprint import pprint
import json


class BambooClient:

    def __init__(self, server: str, username: str, password: str, ssl_verify=True):
        self.bamboo = Bamboo(url=server, username=username, password=password, verify_ssl=ssl_verify)

    def get_plan(self, key: str):
        plan = self.bamboo.get_plan(key)
        json_object = json.dumps(plan, indent=4)
        print(json_object)