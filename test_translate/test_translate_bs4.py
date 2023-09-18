import logging
import os
import re
import requests
from datetime import datetime
from urllib.parse import urlparse

from googletrans import Translator, constants
from bs4 import BeautifulSoup


def get_text_from_html(url):
    logging.getLogger().setLevel(logging.INFO)
    start = datetime.now()
    html = get_html(url)
    trans_start = datetime.now()
    trans_html = get_translated_html(html)
    trans_end = datetime.now()
    save_html(url, html, trans_html)
    end = datetime.now()
    logging.info(f"all process duration : {(end-start).total_seconds()}")
    logging.info(
        f"translate process duration: {(trans_end-trans_start).total_seconds()}"
    )


def get_html(url):
    return requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        },
    ).text


def get_translated_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    elements = soup.find("body").find_all(string=re.compile(".+"))
    for ele in elements:
        text = ele.get_text()
        trans_text = get_translated_text(text).text
        ele.string.replace_with(trans_text)
    return str(soup)


def get_translated_text(texts):
    translator = Translator()
    result = translator.translate(texts, dest="ko")
    return result


def save_html(url, ori_html, trans_html):
    parsed_url = urlparse(url)
    with open(
        os.path.join(
            os.path.abspath(__file__ + "/.."), f"{parsed_url.hostname}_origin.html"
        ),
        "w",
    ) as f:
        f.write(ori_html)
    with open(
        os.path.join(
            os.path.abspath(__file__ + "/.."),
            f"{parsed_url.hostname}_trans.html",
        ),
        "w",
    ) as f:
        f.write(trans_html)


get_text_from_html("https://kiryuu.id")
