import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome("./chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_class_name("search-keyword").send_keys("ber")
# driver.find_element_by_class_name("search-button").click()
time.sleep(4)
veggies = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(veggies)
add_cart_buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for add_cart_button in add_cart_buttons:
    add_cart_button.click()
driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//button[.='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)