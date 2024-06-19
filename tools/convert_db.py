import json
import os
import argparse


def main(args):
    db_path: str = args.db_path
    pack_db: bool = args.minify

    if db_path and os.path.exists(db_path):
        with open(db_path, "r") as db_file:
            content = json.loads(db_file.read())

        with open(db_path, "w") as db_file:
            db_file.write(json.dumps(content,
                                     indent=None if pack_db else 4,
                                     separators=(',', ':')))

    else:
        print("db file doesn't exist")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db_path", type=str, default=None, help="database path", required=True)
    parser.add_argument("--minify", action=argparse.BooleanOptionalAction,
                        type=bool, default=False, help="minify db file", required=False)
    opt = parser.parse_args()

    return opt


if __name__ == '__main__':
    main(get_args())
