from lightberry import Router, Response, typing
from lightberry.shortcuts import jsonify
from crows_nest import db, services_availability_cache
from crows_nest.models import ServiceModel
from crows_nest.resources import ServiceResource

if typing.TYPE_CHECKING:
    from lightberry import Request


services_api = Router("services_api", url_prefix="/api/services")


@services_api.route("/")
async def get_services(request: Request):
    search_name_param: str = request.query_params.get("name")
    sort_param: str = request.query_params.get("sort")

    services: list[ServiceModel] = db.query(ServiceModel,
                                            sort_by={
                                                "key": "added_at",
                                                "type": sort_param
                                            },
                                            search_by={
                                                "name": search_name_param
                                            }
                                            )

    dump_services = ServiceResource(services).dump()
    return Response(payload=jsonify(dump_services))


@services_api.route("/:id")
async def get_service(request, id: str):
    service: ServiceModel | None = db.query(ServiceModel, search_by={"id": int(id)}, first=True)

    if service is None:
        return Response(status_code=404)

    dump_service = ServiceResource(service).dump()
    return Response(payload=jsonify(dump_service))


@services_api.route("/:id/status")
async def check_service_status(request, id: str):
    service: ServiceModel | None = db.query(ServiceModel, search_by={"id": int(id)}, first=True)

    if service is None:
        return Response(status_code=404)

    is_available: bool = services_availability_cache.read(id)
    status = {
        "is_available": is_available if is_available else False
    }

    return Response(payload=jsonify(status))
