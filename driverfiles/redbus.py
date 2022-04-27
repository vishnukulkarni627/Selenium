from time import sleep

from selenium.webdriver import Chrome
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("https://www.makemytrip.com/")
sleep(5)
