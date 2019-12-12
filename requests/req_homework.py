import requests
import json


def get_url(api):
    r = requests.get(api)
    obj = json.loads(r.content)
    return obj


def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)


url = get_url("https://jsonplaceholder.typicode.com/comments")
for n in range(len(url)):
    print(url[n]['name'])
    write_to_file("my_json.json", json.dumps(url[n], sort_keys=True, indent=4), mode='a')
