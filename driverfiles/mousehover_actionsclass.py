from selenium.webdriver import Chrome, ActionChains

driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("https://www.myntra.com/")
a = ActionChains(driver)
profile = driver.find_element_by_xpath("//span[.='Profile']")
a.move_to_element(profile).perform()
driver.find_element_by_xpath("//a[.='login / Signup']").click()