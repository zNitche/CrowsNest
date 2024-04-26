from crows_nest.storage import Database
from crows_nest.storage import Cache

db = Database()
services_availability_cache = Cache()


def create_routers(app):
    from crows_nest.routes import core, api

    app.add_router(api.api)
    app.add_router(api.services_api)

    core.set_catch_all_excluded_routes(app.get_routers_prefixes())
    app.add_router(core)


def setup_tasks(app):
    from crows_nest import tasks
    debug_logging = app.config.get("DEBUG")

    app.add_background_task(tasks.CheckServiceAvailabilityTask(logging=debug_logging))


def setup_app(app):
    db.db_path = app.config.get("DB_PATH")

    create_routers(app)
    setup_tasks(app)
