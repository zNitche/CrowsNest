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


def search_data(raw_data, search_by):
    filtered_data = []

    if search_by:
        for item in raw_data:
            is_matching = True

            for key, value in search_by.items():
                if key and value is not None:
                    item_key_val = item.get(key)
                    check = (value not in item_key_val) if isinstance(value, str) else (value == item_key_val)

                    if not item_key_val or check:
                        is_matching = False

            if is_matching:
                filtered_data.append(item)

    else:
        filtered_data = raw_data

    return filtered_data


def query_models(model, search_by=None, sort_by=None):
    data = read_from(section=model.section_name())
    filtered_data = search_data(data, search_by)

    if sort_by:
        sort_by_key = sort_by["key"]
        sort_by_type = sort_by.get("type") if sort_by["type"] in ["asc", "desc"] else "desc"

        filtered_data.sort(reverse=True if sort_by_type == "desc" else False,
                           key=lambda e: e[sort_by_key])

    models = [model(data=item) for item in filtered_data]

    return models
