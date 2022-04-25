from selenium.webdriver import Chrome
from time import sleep

from selenium.webdriver.support.select import Select

driver = Chrome(r"C:\Users\vishn\PycharmProjects\pythontestingrs\driverfiles\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.find_element_by_link_text("Register")
driver.switch_to_alert().accept()
# NoAlertPresentException occurs