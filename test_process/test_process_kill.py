from selenium import webdriver
import datetime


def run_driver(func):
    import psutil

    driver = webdriver.Chrome("./chromedriver.exe")

    driver.get("https://naver.com")
    for i in psutil.process_iter():
        if "chrome" in i.name() or "Chrome" in i.name():
            print(i)
    print(driver.service.process.pid)
    func(driver.service.process.pid)
    datetime.sleep(3)
    for i in psutil.process_iter():
        if "chrome" in i.name() or "Chrome" in i.name():
            print(i)
    driver.quit()
    print("driver quit")


# def kill_process():
#    processList = psutil.process_iter()
#    for proc in processList:
#        if "Chrome" in proc.name() or "chrome" in proc.name():
#            proc.kill()
#            print("killed")


def killer(x):
    x.kill()
    print("killer")


def kill_process(pid):
    import psutil

    processList = psutil.process_iter()
    for proc in processList:
        if pid == proc.pid:
            children = proc.children()
            print(children)
            datetime.sleep(10)
            for child in children:
                killer(child)
            datetime.sleep(10)
            proc.kill()
            print("killed")


run_driver(kill_process)
# kill_process()
