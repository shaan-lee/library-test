from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://komikstation.co/")

time.sleep(3)

popupPaths = [
    "/html/body/div/div[1]/div/div[3]/span",
    "/html/body/div/div[2]/div/div[3]/span",
    "/html/body/div/div/div/div[3]/span",
]
for popupPath in popupPaths:
    try:
        driver.find_element(By.XPATH, popupPath).click()
        print("팝업 닫기")
    except:
        print("팝업 없음")
driver.quit()
