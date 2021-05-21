import os
import argparse
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


parser = argparse.ArgumentParser(description='Save keys and values')
parser.add_argument('--key', help = 'Save the key into the file', type=str)
parser.add_argument('--val', help = 'Save the value for the due key', type=str)
args = parser.parse_args()

def write_json(person_dict):
    try:
        json_opened = json.load(open(storage_path))
    except:
        json_opened = []
    json_opened.append(person_dict)
    with open(storage_path, 'w') as file:
        json.dump(json_opened, file, indent = 2, ensure_ascii=False)


if args.key and not args.val: #если ввели только key без value
    try:
        json.load(open(storage_path))
    except:
        with open(storage_path, 'w') as file:
            json.dump([], file, indent = 2, ensure_ascii=False)
    with open(storage_path, 'r') as f:
        data = json.load(f)
        list_ = []
        ert = None
        for pair in data:
            if args.key in pair.keys():
                for key_, valu in pair.items():
                    if key_ == args.key:
                        list_.append(valu)
                        if len(list_) > 0:
                            ert = ', '.join(list_)
        print(ert)


if args.key and args.val:
    write_json({args.key : args.val})


