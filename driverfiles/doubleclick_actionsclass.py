from selenium.webdriver import Chrome, ActionChains

driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/demo.html")
a = ActionChains(driver)
dclick_ = driver.find_element_by_xpath("//button[.='Double-click me']")
a.double_click(dclick_).perform()
