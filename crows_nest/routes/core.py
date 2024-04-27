from lightberry import Router, Response, FileResponse
from lightberry.utils import files_utils


core = Router("core")


@core.route("/assets/:asset_name")
async def serve_assets(request, asset_name):
    serialized_path = f"/files/assets/{asset_name.replace('..', '')}"

    if not files_utils.file_exists(serialized_path):
        return Response(status_code=404)

    response = FileResponse(file_path=serialized_path)

    if serialized_path.endswith(".gz"):
        response.add_header("Content-Encoding", "gzip")

    if serialized_path.endswith(".js.gz"):
        response.add_header("Content-Type", "text/javascript")
    elif serialized_path.endswith(".css.gz"):
        response.add_header("Content-Type", "text/css")

    return response


@core.catch_all()
async def web_panel(request):
    if request.url.endswith("favicon.ico"):
        favicon_path = "/files/favicon.ico"

        return FileResponse(file_path=favicon_path) \
            if files_utils.file_exists(favicon_path) else Response(status_code=404)

    return FileResponse(file_path="/files/index.html")
