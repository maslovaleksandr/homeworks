import requests


def get_url(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.headers)
    # print(r.content)


get_url("http://google.com")


