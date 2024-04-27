from lightberry import Router, FileResponse


core = Router("core")


@core.route("/assets/:asset_name")
async def serve_assets(request, asset_name):
    serialized_path = f"/files/assets/{asset_name.replace('..', '')}"
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
        return FileResponse(file_path="/files/favicon.ico")

    return FileResponse(file_path="/files/index.html")
