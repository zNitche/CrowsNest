from lightberry import Router, Response
from lightberry.shortcuts import jsonify
from crows_nest import db, services_availability_cache
from crows_nest.models import ServiceModel
from crows_nest.resources import ServiceResource

api = Router("api", url_prefix="/api")


@api.route("/healthcheck")
async def healthcheck(request):
    return Response(payload="ok")


@api.route("/services/:id")
async def get_service(request, id):
    service = db.query(ServiceModel, search_by={"id": int(id)}, first=True)

    if service is None:
        return Response(status_code=404)

    dump_service = ServiceResource(service).dump()
    return Response(payload=jsonify(dump_service))


@api.route("/services/:id/availability")
async def check_service_availability(request, id):
    service = db.query(ServiceModel, search_by={"id": int(id)}, first=True)

    if service is None:
        return Response(status_code=404)

    is_available = services_availability_cache.read(id)

    return Response(payload=jsonify({"is_available": is_available if is_available else False}))


@api.route("/services")
async def get_services(request):
    search_name_param = request.query_params.get("name")
    sort_param = request.query_params.get("sort")

    services = db.query(ServiceModel,
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
