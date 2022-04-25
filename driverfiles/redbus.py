from time import sleep

from selenium.webdriver import Chrome
driver = Chrome("./chromedriver.exe")
driver.get("https://www.makemytrip.com/")
sleep(5)
