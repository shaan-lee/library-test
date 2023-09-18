#from http_exceptions import HTTPException

#raise HTTPException.from_status_code(status_code = 406)

import requests
res = requests.get("https://httpbin.org/status/500")
res.raise_for_status()
print("pass")