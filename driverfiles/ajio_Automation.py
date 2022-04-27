# 1. Open Ajio website and get the first 6 maximum price of shoes along with the product description.
from selenium.webdriver import Chrome
from time import sleep
import csv
from selenium.webdriver.support.select import Select
from reading_csv import read_

driver = Chrome("../pytestTy/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.ajio.com/")
sleep(5)

d = read_("./ajio.csv")
driver.find_element_by_xpath(d['xpath_search']).send_keys("shoes")
driver.find_element_by_xpath(d['xpath_search_button']).click()
sort_=driver.find_element_by_xpath(d['xpath_dropdown'])
s = Select(sort_)
s.select_by_visible_text("Price (highest first)")
sleep(5)
products = driver.find_elements_by_xpath(d['xpath_product_elements'])
count = 0
n = 6
for product in products:
    count +=1
    if count <= n:
        print(product.text)
        print('--------------------------')
