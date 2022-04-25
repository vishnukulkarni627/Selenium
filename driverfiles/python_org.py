from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
# /session
# link for search engine
# //button[@title='Search with Google or enter address']/div[.='Search with Google or enter address']
driver = Chrome("./chromedriver.exe")
driver.get("https://www.python.org/")
sleep(2)
driver.find_element_by_link_text("Downloads").click()
sleep(2)
driver.find_element_by_xpath("//a[.='Python 3.9.10']/../..//a[.='Release Notes']").click()
