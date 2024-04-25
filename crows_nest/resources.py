from crows_nest import services_availability_cache


class ResourceBase:
    def __init__(self, data):
        self.data = data

    def dump(self):
        pass


class ServiceResource(ResourceBase):
    def __init__(self, data):
        super().__init__(data)

    def __process(self, item):
        is_available = services_availability_cache.read(item.id)
        extra_attrs = {
            "is_available": is_available
        }

        return item.dump(extra_attrs=extra_attrs)

    def __process_many(self):
        dump = [self.__process(service) for service in self.data]
        return dump

    def dump(self):
        if isinstance(self.data, list):
            return self.__process_many()
        else:
            return self.__process(self.data)
