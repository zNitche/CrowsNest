from lightberry import TaskBase
from crows_nest import db, services_availability_cache
from crows_nest.models import ServiceModel
import requests


class CheckServiceAvailabilityTask(TaskBase):
    def __init__(self, logging=False):
        super().__init__(periodic_interval=30, logging=logging)

    async def task(self):
        services: list[ServiceModel] = db.query(ServiceModel)

        for service in services:  # type: ServiceModel
            target_url = f"{service.url}:{service.port}{service.health_check_endpoint}"

            try:
                res = requests.get(url=target_url, timeout=3)
                is_available = True if res.status_code == 200 else False

            except Exception:
                is_available = False

            services_availability_cache.write(service.id, is_available)
