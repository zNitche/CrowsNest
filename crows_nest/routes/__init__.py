from crows_nest.routes.core import core
from crows_nest.routes import api

from lightberry import AppContext

current_app = AppContext.get_current_app()


@current_app.after_request()
async def after_request(response):
    # meant to be LAN only so we don't have to care about strict cors
    response.add_header("Access-Control-Allow-Origin", "*")
    response.add_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
    response.add_header("Access-Control-Allow-Headers", "Content-Type")

    return response
