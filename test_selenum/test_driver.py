from selenium import webdriver
import time


def driver_test():
    driver = webdriver.Chrome("./chromedriver.exe")

    driver.get("https://naver.com")
    time.sleep(20)
    driver.quit()


driver_test()
