import json
from enum import Enum

from tabulate import tabulate


class JsonFormatter:
    def format(self, plans):
        json_object = json.dumps(plans, indent=4)
        print(json_object)


class TableFormatterColumn(Enum):
    KEY = "key"
    NAME = "planName"
    PROJECT = "projectName"
    LINK = "link"


class TableFormatter:
    SUPPORTED_COLUMNS = [column.value for column in TableFormatterColumn]

    def __init__(self, bamboo_base_url, headers=None):
        if headers is None:
            self.headers = [TableFormatterColumn.KEY.value, TableFormatterColumn.NAME.value,
                            TableFormatterColumn.PROJECT.value,
                            TableFormatterColumn.LINK.value]
        else:
            self._check_headers_supported(headers)
            self.headers = headers

        print(self.headers)
        self.bamboo_base_url = bamboo_base_url

    def _check_headers_supported(self, headers):
        for header in headers:
            if header not in self.SUPPORTED_COLUMNS:
                print(f"Header not supported. Please use one of {self.SUPPORTED_COLUMNS}")
                raise NotImplementedError("Not supported header.")

    def format(self, plans):
        print(tabulate(self.plans_to_table(plans), headers=self.headers))

    def plans_to_table(self, plans):
        return [self.as_readable_list(p) for p in plans]

    def as_readable_list(self, plan):
        print(plan._spec)
        return [plan.get(header) if header != TableFormatterColumn.LINK.value else self.get_plan_link(plan) for header in
                self.headers]

    def get_plan_link(self, plan):
        return f"{self.bamboo_base_url}/browse/{plan.get_key()}"
