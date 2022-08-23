from enum import Enum


class Plan:
    def __init__(self, spec: dict) -> None:
        self._spec = spec

    def get(self, key):
        return self._spec[key]

    def get_key(self):
        return self._spec['key']

    def get_name(self):
        return self._spec['planName']

    def get_project_name(self):
        return self._spec['projectName']


class ResourceType(Enum):
    PLAN = ["p", "plan"]
    DEPLOYMENT = ["d", "deployment"]

    @staticmethod
    def from_str(s):
        if s in ResourceType.PLAN.value:
            return ResourceType.PLAN
        elif s in ResourceType.DEPLOYMENT.value:
            return ResourceType.DEPLOYMENT
        else:
            raise NotImplementedError("Unknown resource type: " + s)
