def create_routers(app):
    from crows_nest.routes import core, api

    app.add_router(api)

    core.set_catch_all_excluded_routes(app.get_routers_prefixes())
    app.add_router(core)


def setup_app(app):
    create_routers(app)
