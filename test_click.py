import logging as log
import coloredlogs
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.chrome.options import Options
import traceback

coloredlogs.install(
    level="DEBUG", fmt="[%(asctime)s][%(process)d] %(levelname)s %(message)s"
)


def sleep2():
    driver = webdriver.Chrome("./chromedriver.exe")

    driver.get("https://naver.com")
    test = 1000
    datetime.sleep(1)
    print("sleep")
    log.info("log test")
    driver.quit()


def sleep1():
    testtest = 111
    sleep2()
    datetime.sleep(5)
    driver.quit()
