from time import sleep
from selenium.webdriver import Chrome
driver = Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.find_element_by_xpath("//input[@value='Search']").click()
driver.switch_to.alert.accept()