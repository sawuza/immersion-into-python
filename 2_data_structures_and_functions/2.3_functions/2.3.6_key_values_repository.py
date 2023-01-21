import argparse
import tempfile
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key', default=None, type=str)
parser.add_argument('--value', default=None, type=str)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def read_json():
    with open(storage_path, 'r', encoding='utf-8') as f:
        reading = json.load(f)
        return reading


def write_json():
    with open(storage_path, 'r+', encoding='utf-8') as f:
        data = f.read().strip()
        if len(data) <= 0:
            storage_dict = {}
        else:
            storage_dict = json.loads(data)

        if args.key in storage_dict and len(storage_dict[args.key]) > 0:
            storage_dict[args.key].append(args.value)
        else:
            storage_dict[args.key] = [args.value]
        res = json.dumps(storage_dict)
        f.seek(0)
        f.write(res)
        f.close()


if args.value != None:
    if not os.path.exists(storage_path):
        open(storage_path, 'a').close()
    write_json()

if args.value == None:
    res = None
    if os.path.exists(storage_path):
        storage_dict = read_json()
        if args.key in storage_dict:
            res = storage_dict[args.key]
            print(', '.join(res))
        else:
            print(res)
