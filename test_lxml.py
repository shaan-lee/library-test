import requests
from lxml import etree

html = requests.get(
    "https://kiryuu.id",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    },
).text
root = etree.HTML(html)
print(root.xpath("//li"))
