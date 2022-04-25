from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
a = ActionChains(driver)
a.send_keys(Keys.PAGE_DOWN).perform()