import urllib
import json
import os
from bs4 import BeautifulSoup


def fetch(url):
    _, filename = os.path.split(url)
    path = os.path.join("cache", filename)
    if not os.path.exists(path):
        urllib.urlretrieve(url, path)
    return filename, path

LICENSES = []

for line in open("licenses/all.txt"):
    url, name = line.strip().split(" ", 1)
    title, filename = fetch("http://www.opensource.org" + url.replace("\"", ""))

    try:
        soup = BeautifulSoup(open(filename))
    except:
        continue

    pre = soup.find("pre")


    if pre:
        LICENSES.append({
            'name': title,
            'description': name,
            'txt': pre.text,
            })

print json.dumps(LICENSES, indent=4)
