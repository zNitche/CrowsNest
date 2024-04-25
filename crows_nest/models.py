class ModelBase:
    @staticmethod
    def section_name():
        return None

    def __init__(self, data=None):
        self.id = None

        if data:
            self.__setup_data(data)

    def __setup_data(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def dump(self):
        return {}


class ServiceModel(ModelBase):
    @staticmethod
    def section_name():
        return "services"

    def __init__(self,
                 name=None,
                 added_at=None,
                 url=None,
                 port=None,
                 health_check_endpoint=None,
                 data=None):

        self.name = name
        self.added_at = added_at
        self.url = url
        self.port = port
        self.health_check_endpoint = health_check_endpoint

        super().__init__(data)

    def dump(self):
        return {
            "name": self.name,
            "added_at": self.added_at,
            "url": self.url,
            "port": self.port,
            "health_check_endpoint": self.health_check_endpoint
        }
