import configparser
import requests
import datetime
from urllib.parse import urlparse, urlencode
from datetime import datetime

config = configparser.ConfigParser()
config.read(".cfg")
config = config["MELON"]

params = {"pageSize": 50, "areaFlg": "I", "startIndex": 400001}
start = datetime.time()
start_time = datetime.now()
count = 0
sleep_time = 17
proxy_addr = config["proxy"]
while True:
    base_url = "https://www.melon.com/new/listPaging.htm"
    res = requests.get(
        url=f"{base_url}?{urlencode(params)}",
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        },
        proxies={"https": proxy_addr},
    )
    print(res.status_code)
    print(res.url)
    params["startIndex"] -= params["pageSize"]
    if res.status_code != 200:
        end = datetime.time()
        end_time = datetime.now()
        print(
            "\nsleep time:",
            sleep_time,
            "\nproxy addr:",
            proxy_addr,
            "\nduration:",
            end - start,
            "\nstart time:",
            start_time,
            "\nend time:",
            end_time,
            "\ncount:",
            count,
        )
        break
    count += 1
    datetime.sleep(sleep_time)
