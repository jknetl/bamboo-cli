class Plan:
    def __init__(self, spec: dict) -> None:
        self._spec = spec

    def get_key(self):
        return self._spec['key']

    def get_name(self):
        return self._spec['planName']

    def get_project_name(self):
        return self._spec['projectName']


    # TODO: move this to some kind of formatter
    def as_readable_list(self):
        return [self.get_key(), self.get_name(), self.get_project_name()]
