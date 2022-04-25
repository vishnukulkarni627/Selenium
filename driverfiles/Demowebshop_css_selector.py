from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
sleep(5)
driver.find_element_by_css_selector("a[class='ico-register']").click()
# driver.find_element_by_css_selector("input[value='M']").click()
driver.find_element_by_css_selector("input[name='FirstName']").send_keys("hello")
driver.find_element_by_css_selector("input[name='LastName']").send_keys("world")
driver.find_element_by_css_selector("input[name='Email']").send_keys("hello123@gmail.com")
driver.find_element_by_css_selector("input[name='Password']").click()






