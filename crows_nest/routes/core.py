from lightberry import Router, FileResponse, typing

if typing.TYPE_CHECKING:
    from lightberry import Request


core = Router("core")


@core.route("/assets/:asset_name")
async def serve_assets(request: Request, asset_name: str):
    serialized_path = f"/files/assets/{asset_name.replace('..', '')}"

    return FileResponse(file_path=serialized_path)


@core.catch_all()
async def web_panel(request: Request):
    return FileResponse(file_path="/files/index.html")
