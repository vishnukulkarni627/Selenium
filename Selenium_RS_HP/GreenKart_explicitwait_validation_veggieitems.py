import re
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
l =[]
l1 = []
driver = Chrome("./chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_class_name("search-keyword").send_keys("ber")
# driver.find_element_by_class_name("search-button").click()
time.sleep(4)
veggies = (driver.find_elements_by_xpath("//div[@class='products']/div"))
# veg_names= driver.find_elements_by_xpath("//div[@class='product']//h4")
# for veg_name in veg_names:
#     # print(veg_name.text)
#     match = re.findall(r'[a-zA-Z]+', veg_name.text)
#     l.append(match[0])
# print(l)
add_cart_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for add_cart_button in add_cart_buttons:
    match1 = re.findall(r'[a-zA-Z]+', add_cart_button.find_element_by_xpath("parent::div/parent::div/h4").text)
    # l.append(add_cart_button.find_element_by_xpath("parent::div/parent::div/h4").text)  # Without removing weights
    l.append(match1[0])  # Only product name
    add_cart_button.click()
print(l)
driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//button[.='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))
veg_names_after = driver.find_elements_by_xpath("//p[@class='product-name']")
for veg_name_after in veg_names_after:
    match2 = re.findall(r'[a-zA-Z]+', veg_name_after.text)
    # l1.append(veg_name_after.text)
    l1.append(match2[0])
print(l1)
assert l == l1
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)

