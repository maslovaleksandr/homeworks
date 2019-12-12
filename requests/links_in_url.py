import requests
import re


r = requests.get("https://habrahabr.ru/")

link = r"<a href=.*>"
urls = re.findall(link, r.text)

for url in urls:
    with open("link_on_habr.txt", mode='a') as f:
        f.write(url + "\n")

