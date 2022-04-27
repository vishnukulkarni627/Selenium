from selenium.webdriver import Chrome, ActionChains

driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
reg_=driver.find_element_by_xpath("//a[.='Register']")
a = ActionChains(driver)
a.context_click(reg_).perform()
