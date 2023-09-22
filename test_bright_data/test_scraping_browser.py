import logging as log
import sys
from pathlib import Path

import requests
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import configparser

logger = log.getLogger()
handler = log.StreamHandler(sys.stdout)
handler.setLevel("INFO")
logger.setLevel("INFO")
logger.addHandler(handler)

dir_path = Path("").absolute()

config = configparser.ConfigParser()
config.read(".cfg")
config = config["BRIGHT_DATA"]
AUTH = config["auth"]
sbr_webdriver = f"https://{AUTH}@zproxy.lum-superproxy.io:9515"


test_url = "https://www.collinsdictionary.com/dictionary/korean-english/%EC%98%AC%EB%B9%BC%EB%AF%B8"


def driver_test():
    sbr_connection = ChromiumRemoteConnection(sbr_webdriver, "goog", "chrome")
    sbr_start = datetime.now()
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(test_url)
        driver.get_screenshot_as_file(
            f"{str(dir_path)}/test_bright_data/scraping_browser_test.png"
        )
    sbr_duration = datetime.now() - sbr_start

    selenium_start = datetime.now()
    with Chrome(service=Service(ChromeDriverManager().install())) as driver:
        driver.get(test_url)
        driver.get_screenshot_as_file(
            f"{str(dir_path)}/test_bright_data/selenium_test.png"
        )
    selenium_duration = datetime.now() - selenium_start

    logger.info("sbr duration:%s", sbr_duration)
    logger.info("selenium duration:%s", selenium_duration)


driver_test()
