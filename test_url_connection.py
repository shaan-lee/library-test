import os
import requests

with open(
    os.path.join(os.path.abspath(__file__ + "/.."), "test_connection.txt"), "r"
) as f:
    urls = f.read().splitlines()

for url in urls:
    try:
        res = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            },
            timeout=20,
        )
        res.raise_for_status()
    except:
        with open(
            os.path.join(
                os.path.abspath(__file__ + "/.."), "connection_error_site.txt"
            ),
            "a",
        ) as f:
            f.write(f"{url}\t{res.status_code}\n")
            print(url)
