from selenium.webdriver import Chrome
from time import sleep
driver = Chrome('./chromedriver.exe')
driver.get("https://www.flipkart.com/")
sleep(2)
driver.maximize_window()
driver.find_element_by_xpath("//button[.='✕']").click()
driver.find_element_by_xpath("//input[@title='Search for products, brands and more']").send_keys("laptops")
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(7)
driver.find_element_by_xpath("//div[@class='_4rR01T']").click()
sleep(3)
ids = driver.window_handles
print(ids)
driver.switch_to.window(ids[1])
driver.find_element_by_xpath("//input[@id='pincodeInputId']").send_keys("560090")
driver.find_element_by_xpath("//span[@class='_2P_LDn']").click()
sleep(2)
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2U9uOA _3v1-ww']/..").click()
