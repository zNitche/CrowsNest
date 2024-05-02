import json
from lightberry.utils import files_utils
from lightberry import typing

if typing.TYPE_CHECKING:
    from typing import Type
    from crows_nest.models import ModelBase


class Database:
    def __init__(self):
        self.db_path: str | None = None

    def __read_from(self, section: str | None = None, raise_exception=True) -> dict[str, ...] | None:
        if raise_exception:
            if not self.db_path or not files_utils.file_exists(self.db_path):
                raise Exception("db file is unavailable")

        with open(self.db_path, "r") as db_file:
            content = json.loads(db_file.read())

        return content.get(section) if section else content

    def __search_data(self, raw_data: dict[str, ...], search_by: dict[str, ...]) -> list[dict[str, ...]]:
        filtered_data: list[dict[str, ...]] = []

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
            filtered_data = [item for item in raw_data]

        return filtered_data

    def query(self,
              model: Type[ModelBase],
              search_by: dict[str, ...] | None = None,
              sort_by: dict[str, str] = None,
              first=False) -> list[ModelBase] | ModelBase:

        models = []
        data = self.__read_from(section=model.section_name())

        if data is not None:
            filtered_data = self.__search_data(data, search_by)

            if sort_by:
                sort_by_key = sort_by["key"]
                sort_by_type = sort_by.get("type") if sort_by["type"] in ["asc", "desc"] else "desc"

                filtered_data.sort(reverse=True if sort_by_type == "desc" else False,
                                   key=lambda e: e[sort_by_key])

            for index, item in enumerate(filtered_data):
                item_model = model()
                item_model.create(item)

                models.append(item_model)

                if index == 0 and first:
                    break

        return models
