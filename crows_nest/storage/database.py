import json
from lightberry.utils import files_utils


class Database:
    def __init__(self):
        self.db_path = None

    def __read_from(self, section=None, raise_exception=True):
        if raise_exception:
            if not self.db_path or not files_utils.file_exists(self.db_path):
                raise Exception("db file is unavailable")

        with open(self.db_path, "r") as db_file:
            content = json.loads(db_file.read())

        return content.get(section) if section else content

    def __search_data(self, raw_data, search_by):
        filtered_data = []

        if search_by:
            for item in raw_data:
                is_matching = True

                for key, value in search_by.items():
                    if key and value is not None:
                        item_key_val = item.get(key)
                        check = (value in item_key_val) if isinstance(value, str) else (value == item_key_val)

                        if item_key_val is None or not check:
                            is_matching = False

                if is_matching:
                    filtered_data.append(item)

        else:
            filtered_data = raw_data

        return filtered_data

    def query(self, model, search_by=None, sort_by=None, first=False):
        data = self.__read_from(section=model.section_name())
        filtered_data = self.__search_data(data, search_by)

        if sort_by:
            sort_by_key = sort_by["key"]
            sort_by_type = sort_by.get("type") if sort_by["type"] in ["asc", "desc"] else "desc"

            filtered_data.sort(reverse=True if sort_by_type == "desc" else False,
                               key=lambda e: e[sort_by_key])

        models = []

        for item in filtered_data:
            item_model = model()
            item_model.create(item)

            models.append(item_model)

        if first:
            models = models[0] if len(models) > 0 else None

        return models
