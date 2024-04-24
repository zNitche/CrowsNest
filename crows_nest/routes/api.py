from lightberry import Router, Response, shortcuts
from crows_nest import db


api = Router("api", url_prefix="/api")


@api.route("/healthcheck")
async def healthcheck(request):
    return Response(payload="ok")


@api.route("/services")
async def get_services(request):
    search_name_param = request.query_params.get("name")
    sort_param = request.query_params.get("sort")
    sort_param = sort_param if sort_param in ["asc", "desc"] else "desc"

    services = db.read_from("services")

    services = services if services else []
    services.sort(reverse=True if sort_param == "desc" else False,
                  key=lambda e: e["addedAt"])

    filtered_services = []

    if search_name_param:
        for service in services:
            if service["name"].startswith(search_name_param):
                filtered_services.append(service)

    else:
        filtered_services = services

    return Response(payload=shortcuts.jsonify(filtered_services))
