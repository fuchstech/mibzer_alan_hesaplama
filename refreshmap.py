from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
from time import sleep


def runmap():
    service = Service(executable_path="/home/fuchs/Desktop/Python-Selenium-Google-Form automation/chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=service)
    while 1:
        url = "file:///home/fuchs/Desktop/ekimmakinas%C4%B1/pygmap1.html"
        driver.get(url)
        driver.refresh()
        #pyautogui.press("F11")
        sleep(7)
if __name__ == "__main__":
    runmap()
