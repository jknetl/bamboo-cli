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


