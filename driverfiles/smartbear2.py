import re
from time import sleep

from selenium.webdriver import Chrome
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
element_items = driver.find_elements_by_xpath("//h3[@class='art-name']/a/span")
element_prices = driver.find_elements_by_xpath("//span[@class='art-price' or @class='art-price art-price--offer']")
# getting text of each product
all_items = [element.text for element in element_items]
all_prices = []
# Getting actual price
for element_price in element_prices:
    actual_prices = element_price.text
    actual_price = float("".join(re.findall(r"[\d\.]", actual_prices)))
    all_prices.append(actual_price)
actual_pricess = {}
for product, price in zip(all_items,all_prices):
    actual_pricess[product] = price
# print(actual_pricess)
# products with less than 100
less_100 = {product : price for product,price in actual_pricess.items() if price < 100}
print(less_100)