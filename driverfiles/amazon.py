from time import sleep

from selenium.webdriver import Chrome
driver = Chrome("./chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("mobiles")
driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()
driver.find_element_by_xpath("//div[@class='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right']/div/div/div/h2/a").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
driver.find_element_by_xpath("//input[@name='submit.add-to-cart']").click()
sleep(3)
driver.find_element_by_xpath("//form[@id='attach-view-cart-button-form']").click()