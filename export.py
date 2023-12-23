# Exports data to _redirect file
from json import load

with open("data.json") as d:
    data = load(d)

redirects = []
for d in data:
    redirects.append(f"/{d['slug']} https://{d['url']} 301")

with open("_redirects", "w") as r:
    r.write("\n".join(redirects))