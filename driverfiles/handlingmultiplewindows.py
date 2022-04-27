from time import sleep

from selenium.webdriver import Chrome
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.find_element_by_xpath("//a[.='Twitter']").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
sleep(5)
driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("hi")
sleep(5)
driver.switch_to.window(ids[0])
sleep(2)
driver.find_element_by_xpath("//a[.='Register']").click()
