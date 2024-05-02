from lightberry import typing

if typing.TYPE_CHECKING:
    pass


class ModelBase:
    @staticmethod
    def section_name() -> str | None:
        return None

    def __init__(self):
        self.id: int | None = None

    def create(self, data: dict[str, ...]):
        self.__setup_data(data)

    def __setup_data(self, data: dict[str, ...]):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def dump(self, extra_attrs: dict[str, ...] = None) -> dict[str, ...]:
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
                 name: str | None = None,
                 added_at: str | None = None,
                 url: str | None = None,
                 redirect_url: str | None = None,
                 port: int | None = None,
                 health_check_endpoint: str | None = None,):

        super().__init__()

        self.name = name
        self.added_at = added_at
        self.url = url
        self.redirect_url = redirect_url
        self.port = port
        self.health_check_endpoint = health_check_endpoint

    def dump(self, extra_attrs=None):
        data = super().dump(extra_attrs)

        data["name"] = self.name
        data["added_at"] = self.added_at
        data["url"] = self.url
        data["redirect_url"] = self.redirect_url
        data["port"] = self.port
        data["health_check_endpoint"] = self.health_check_endpoint

        return data
