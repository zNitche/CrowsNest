from lightberry import AppContext
from lightberry.utils import files_utils
import json


def read_from(section=None, raise_exception=True):
    app = AppContext.get_current_app()
    db_path = app.config.get("DB_PATH")

    if raise_exception:
        if not db_path or not files_utils.file_exists(db_path):
            raise Exception("db file is unavailable")

    with open(db_path, "r") as db_file:
        content = json.loads(db_file.read())

    return content.get(section) if section else content
