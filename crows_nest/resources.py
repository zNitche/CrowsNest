from crows_nest import services_availability_cache
from lightberry import typing

if typing.TYPE_CHECKING:
    from crows_nest.models import ServiceModel


class ResourceBase:
    def __init__(self, data):
        self.data = data

    def dump(self):
        pass


class ServiceResource(ResourceBase):
    def __init__(self, data: ServiceModel | list[ServiceModel]):
        super().__init__(data)

    def __process(self, item: ServiceModel) -> dict[str, ...]:
        is_available: bool = services_availability_cache.read(item.id)
        extra_attrs = {
            "is_available": is_available
        }

        return item.dump(extra_attrs=extra_attrs)

    def __process_many(self) -> list[dict[str, ...]]:
        dump = [self.__process(service) for service in self.data]
        return dump

    def dump(self) -> dict[str, ...] | list[dict[str, ...]]:
        if isinstance(self.data, list):
            return self.__process_many()
        else:
            return self.__process(self.data)
