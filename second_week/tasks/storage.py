import argparse
import json
import os
import tempfile


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--value")
    return parser.parse_args()


def add_to_storage(key, value):
    storage_path = get_storage_path()
    storage_data = read_storage_file(storage_path)
    with open(storage_path, 'w') as f:
        if storage_data:
            json_data = json.loads(storage_data)
            if key in json_data:
                json_data[key].append(value)
            else:
                json_data[key] = [value]
            f.write(json.dumps(json_data))
        else:
            f.write(json.dumps({key: [value]}))


def read_storage_file(storage_path):
    if os.path.isfile(storage_path):
        with open(storage_path, 'r') as f:
            storage_content = f.read()
            return storage_content


def get_storage_path():
    return os.path.join(tempfile.gettempdir(), 'storage.data')


def get_from_storage(key):
    storage_path = get_storage_path();
    storage_data = read_storage_file(storage_path)
    if storage_data:
        json_data = json.loads(storage_data)
        if key in json_data:
            return json_data[key]


if __name__ == "__main__":
    args = parse_args()
    if args.value:
        add_to_storage(args.key, args.value)
    else:
        value = get_from_storage(args.key)
        if value:
            print(", ".join(value))
        else:
            print(None)

