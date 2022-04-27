import re
l=[]
all_items= {}
from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("https://www.myntra.com/")
driver.find_element_by_xpath("//input[@class='desktop-searchBar']").send_keys("men shirts")
driver.find_element_by_xpath("//a[@class='desktop-submit']").click()
shirt_names = driver.find_elements_by_xpath("//h3[@class='product-brand']")
all_shirt_names = [shirt_name.text for shirt_name in shirt_names]
shirt_prices = driver.find_elements_by_xpath("//div[@class='product-price']")
all_shirt_prices = [shirt_price.text for shirt_price in shirt_prices]
for i in all_shirt_prices:
    res = (re.findall(r"\b\d{3,4}", i))
    l.append(int(res[0]))
for shirt, price in zip(all_shirt_names, l):
    all_items[shirt] = price
less_1000 = {shirt: price for shirt, price in all_items.items() if price<1500 }
print(less_1000)

