import requests

res = requests.get(
    "https://hangeul.naver.com/hangeul_static/webfont/zips/nanum-gothic.zip"
)
file = res.content
