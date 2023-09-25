from selenium import webdriver
from selenium.webdriver import Keys, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui


def driver_test():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = ActionChains(driver)

    driver.get(
        "https://stackoverflow.com/questions/34222412/load-chrome-extension-using-selenium"
    )
    action.context_click().perform()
    for _ in range(8):
        pyautogui.hotkey("down")
    pyautogui.hotkey("enter")

    time.sleep(10)
    driver.quit()


driver_test()
