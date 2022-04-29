from time import sleep
from selenium.webdriver import Chrome
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.find_element_by_xpath("//input[@value='Search']").click()
sleep(5)
driver.switch_to.alert.accept()