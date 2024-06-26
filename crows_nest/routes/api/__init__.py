from lightberry import Router, Response
from crows_nest.routes.api.services import services_api
from crows_nest.routes.api.sensors import sensors_api


api = Router("api", url_prefix="/api")


@api.route("/healthcheck")
async def healthcheck(request):
    return Response(payload="ok")
