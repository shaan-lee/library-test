from selenium import webdriver
import datetime


def driver_test():
    driver = webdriver.Chrome("./chromedriver.exe")

    driver.get("https://naver.com")
    datetime.sleep(20)
    driver.quit()


driver_test()
