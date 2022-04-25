from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
sleep(2)
products = ['14.1-inch Laptop']
for product in products:
    driver.find_element_by_xpath(f"//a[.='{product}']/../..//input[@value='Add to cart']").click()
