import json
from func_for_files import open_file

if __name__ == '__main__':
    data = open_file("data.json")

    # from string to object
    obj = json.loads(data)
    print(obj, type(obj))
    print(obj['name'])


    # from object to json
    print()
    obj['new-value'] = 'secret'
    print(json.dumps(obj, sort_keys=True, indent=4))
