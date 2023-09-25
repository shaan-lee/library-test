from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib


def tmp():
    driver = webdriver.Chrome("./chromedriver.exe")

    driver.get("https://www.qyy158.com/info/10270/2055210.html")

    imgs = driver.find_elements(By.XPATH, "/html/body/div[5]/img")
    urls = []
    i = 0
    for img in imgs:
        urls.append(img.get_attribute("data-original"))
    for url in urls:
        i += 1
        if i >= 3:
            break
        urllib.request.urlretrieve(url, f"{i}.png")

    driver.quit()
