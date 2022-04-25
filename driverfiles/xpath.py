from selenium.webdriver import Chrome
from time import sleep
# /session
driver = Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/xpath.html")
# Absolute Xpath: This xpath is very tedious to trace. Because traversing is from parent to immediate child
# In order to overcome this problem we go for relative xpath
driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys("vishnu")
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/input[2]").send_keys("kulkarni")
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/input[1]").send_keys("tyss")
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/input[2]").send_keys("bangalore")
sleep(2)
driver.close()
# Relative xpath: General syntax --- //html_tag[@attribute_name = 'attribute_value']

