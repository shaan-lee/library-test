import requests
from urllib.parse import urlencode
def send_get():
    param = {"updated_at":{"$gte":"2023-08-20","$lt":"2023-08-25"}}
    url_param = urlencode(param)
    print(url_param)
    data = requests.get(f"http://localhost:5003/api/v1/sites?{url_param}")
    print(data.content)
    
send_get()