# 1. Open Ajio website and get the first 6 maximum price of shoes along with the product description.
import re

from selenium.webdriver import Chrome
from time import sleep
import csv
from selenium.webdriver.support.select import Select
from reading_csv import read_

driver = Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts/")
sleep(5)

d = read_("./smartbear.csv")   # Pass the product prices which will be in csv format

for item, expected_price in d.items():
    sleep(1)
    _xpath= f"//span[.='{item}']/../../..//span[@class='art-price' or @class='art-price art-price--offer']"
    actual_price = driver.find_element_by_xpath(_xpath).text
    actual_price = float("".join(re.findall(r"[\d\.]", actual_price)))
    sleep(1)
    if float(expected_price) == actual_price:
        print('pass')
    else:
        print('fail')
