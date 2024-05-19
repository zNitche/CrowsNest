from lightberry import Router, FileResponse, typing

if typing.TYPE_CHECKING:
    from lightberry import Request


core = Router("core")


@core.route("/assets/:asset_name")
async def serve_assets(request: Request, asset_name: str):
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
async def web_panel(request: Request):
    asset_path = "/files/index.html"

    return FileResponse(file_path=asset_path)
