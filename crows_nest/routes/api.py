from lightberry import Router, Response


api = Router("api", url_prefix="/api")


@api.route("/healthcheck")
async def healthcheck(request):
    return Response(payload="ok")
