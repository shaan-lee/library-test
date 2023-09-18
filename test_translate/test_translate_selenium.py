import logging
import os
from datetime import datetime
import re

from googletrans import Translator

import selenium
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_browser_window(url):
    logging.getLogger().setLevel(logging.INFO)
    start = datetime.now()
    driver = run_selenium()
    driver.get(url)
    texts = driver.find_elements(
        By.XPATH,
        "//body//*[normalize-space(text())!=''][not(self::script)][not(self::style)]",
    )
    trans_start = datetime.now()
    for text in texts:
        try:
            string = text.text
            if not string:
                continue
        except:
            continue
        trans_string = translate(string)
        driver.execute_script(
            "arguments[0].innerText = arguments[1]", text, trans_string
        )
    trans_end = datetime.now()
    with open(
        os.path.join(
            os.path.abspath(__file__ + "/.."), url.replace("/", "|") + ".html"
        ),
        "w",
    ) as f:
        f.write(driver.page_source)
    driver.quit()
    end = datetime.now()
    logging.info(f"all process duration: {(end-start).total_seconds()}")
    logging.info(
        f"translate process duration: {(trans_end-trans_start).total_seconds()}"
    )


def run_selenium():
    chromeDriverManager = ChromeDriverManager()
    options = ChromeOptions()
    return selenium.webdriver.Chrome(
        service=ChromeService(chromeDriverManager.install()), options=options
    )


def translate(string: str):
    translator = Translator()
    return translator.translate(string, dest="ko").text


get_browser_window("https://kiryuu.id")
