from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome("./chromedriver.exe")
driver.get("http://122.166.192.191:9003/")
driver.find_element_by_link_text("Signup").click()
driver.find_element_by_id("select2-gender-container").click()
# for gender in genders:
#     print(gender.text)
sleep(2)
driver.find_element_by_xpath("//ul[@class='select2-results__options']//li[contains(text(),'Mr')]").click()


