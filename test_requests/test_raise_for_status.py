import requests

def get_res(url:str):
    res = requests.get(url)
    res.raise_for_status()
    print("============")
    print(res.status_code)

get_res("https://httpbin.org/status/503")