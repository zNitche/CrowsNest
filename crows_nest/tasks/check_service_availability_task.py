from lightberry import ATaskBase
from crows_nest import db, services_availability_cache
from crows_nest.models import ServiceModel
from microHTTP import MicroHttpClient


class CheckServiceAvailabilityTask(ATaskBase):
    def __init__(self, logging=False):
        super().__init__(periodic_interval=15, logging=logging)

        self.http_client = MicroHttpClient()

    async def task(self):
        services: list[ServiceModel] = db.query(ServiceModel)

        for service in services:  # type: ServiceModel
            try:
                res = await self.http_client.get(host=service.url,
                                                 url=service.health_check_endpoint,
                                                 port=int(service.port),
                                                 timeout=3)

                is_available = True if res.status_code == 200 else False

            except Exception:
                is_available = False

            services_availability_cache.write(service.id, is_available)
