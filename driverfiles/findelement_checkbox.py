from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
# /session
# link for search engine
# //button[@title='Search with Google or enter address']/div[.='Search with Google or enter address']
driver = Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/demo.html")
# driver.find_element_by_xpath("(//input[@name='download'])[4]").click()
# the above xpath has some drawback if dev changes to the html file we might be lead to failure of clicking python
# respective checkbox
#  Using text in xpath --- Syntax --- //tagname[text()='actual_text']
sleep(2)
driver.find_element_by_xpath("//td[.='Python']/..//input[@name='download']").click()
# the above xpath shows us that //td[.='Python'] is independent and we have move to parent of that /.. and attach xpath
#of checkbox
# 1. Check for Dependent and Independent elements
# 2. Write the xpath of independent element and move to the html tree till sucgh point where
# both dependent and independent are getting covered under common node or parent
# 3. write xpath of dependent element