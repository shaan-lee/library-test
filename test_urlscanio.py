import time
import requests
import json
from configparser import ConfigParser

config = ConfigParser()
config.read(".cfg")
config = config["URLSCANIO"]

scan_url = "https://kiryuu.id/star-martial-god-technique-chapter-657/"

headers = {
    "API-Key": config["api_key"],
    "Content-Type": "application/json",
}
data = {
    "url": scan_url,
    "visibility": "public",
}
response = requests.post(
    "https://urlscan.io/api/v1/scan/", headers=headers, data=json.dumps(data)
)
print(response)
res_content = response.json()
print(res_content)
result_uuid = res_content["uuid"]
result_base_url = "https://urlscan.io/api/v1/result"
result = requests.get(f"{result_base_url}/{result_uuid}")
while result.status_code != 200:
    time.sleep(1)
    result = requests.get(f"{result_base_url}/{result_uuid}")
result_content = result.content.decode("utf-8")

data = json.loads(result_content)["data"]
data_requests = data["requests"]
save_file_name = scan_url.replace("/", "|")
for request in data_requests:
    raw_request = request["request"]
    request = raw_request["request"]
    if "isSameSite" in request:
        if not request["isSameSite"] is True:
            with open(f"./{save_file_name}.jsonl", "a") as f:
                f.write(json.dumps(raw_request))
                f.write("\n")
