import configparser

from serpapi import GoogleSearch

config = configparser.ConfigParser()
config.read(".cfg")
config = config["SERPAPI"]

params = {
    "engine": "google_lens",
    "url": "https://www.shinailbo.co.kr/news/photo/201411/416028_220169_527.jpg",
    "api_key": config["api_key"],
}

search = GoogleSearch(params)
result = search.get_dict()
visual_matches = result["visual_matches"]
print(visual_matches)
