import time
import pickle
import os
from configparser import ConfigParser
from selenium.webdriver import Chrome
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

config = ConfigParser()
config.read(".cfg")
config = config["INSTAGRAM"]

SEARCH_URL = "https://www.instagram.com/"
SELENIUM_SESSION_FILE = "./instagram_cookies.pkl"


def get_hashtagged_post_text(search_query):
    driver = get_driver()
    login_site(driver)
    driver.get(get_search_page(search_query))
    time.sleep(2)
    post_list = driver.find_elements(By.XPATH, "//div[@class='_aabd _aa8k  _al3l']/a")
    driver.get(post_list[0].get_attribute("href"))
    time.sleep(2)
    post_text = driver.find_element(
        By.XPATH, "//div[@class='x78zum5 xdt5ytf x1iyjqo2']//span[./a]"
    )
    print(post_text.text)
    time.sleep(5)
    driver.quit()


def get_driver():
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    )
    driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    return driver


def login_site(driver):
    driver.get(SEARCH_URL)
    if os.path.exists(SELENIUM_SESSION_FILE):
        cookies = pickle.load(open(SELENIUM_SESSION_FILE, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get(SEARCH_URL)
    else:
        time.sleep(5)
        username_input = driver.find_element(By.XPATH, "//input[@name='username']")
        password_input = driver.find_element(By.XPATH, "//input[@name='password']")
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        username_input.send_keys(config["username"])
        password_input.send_keys(config["password"])
        submit_button.click()
        time.sleep(2)
        save_session_button = driver.find_element(By.XPATH, "//button[@type='button']")
        save_session_button.click()
    pickle.dump(driver.get_cookies(), open(SELENIUM_SESSION_FILE, "wb"))


def get_search_page(search_query):
    return "https://www.instagram.com/explore/tags/" + search_query


get_hashtagged_post_text("드라마")
