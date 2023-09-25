import logging as log
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

######################################

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def go_to_url(url):
    limit_cnt = 0
    while True and limit_cnt < 3:
        try:
            if url.startswith("javascript"):
                log.warning("요청할 수 없는 url : %s", url)
                return False
            log.info("접속 시도 : %s", url)
            driver.get(url)
        except Exception:
            log.warning("요청에러 다시 시도 : %s", url)
            time.sleep(5)
            limit_cnt += 1
            continue
        break
    driver.quit()


go_to_url("https://naver.com")
