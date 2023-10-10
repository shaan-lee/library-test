import logging as log
import time
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

######################################


def get_content_imgs(site_url):
    img_srcs = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(site_url)
    while True:
        imgs = driver.find_elements(By.XPATH, "//div[@class='bsx']/a/div/img")
        for img in imgs:
            img_srcs.append(img.get_attribute("src"))
        try:
            next_button = driver.find_element(
                By.XPATH, "//div[@class='hpage']/a[@class='r']"
            )
            next_page = next_button.get_attribute("href")
            driver.get(urljoin(site_url, next_page))
        except:
            break
    log.info(img_srcs)


get_content_imgs("https://noromax.my.id/Komik/")
