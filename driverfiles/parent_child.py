from selenium.webdriver import Chrome
from time import sleep
import csv
from selenium.webdriver.support.select import Select
from reading_csv import read_

driver = Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get("file:///C:/Users/vishn/Downloads/demo-html/parent_child.html")
sleep(2)
