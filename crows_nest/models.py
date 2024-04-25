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

    def dump(self, extra_attrs=None):
        data = {}

        if extra_attrs is not None:
            for key, value in extra_attrs.items():
                data[key] = value

        return data


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

    def dump(self, extra_attrs=None):
        data = super().dump(extra_attrs)

        data["name"] = self.name
        data["added_at"] = self.added_at
        data["url"] = self.url
        data["port"] = self.port
        data["health_check_endpoint"] = self.health_check_endpoint

        return data
