from selenium.webdriver import Chrome
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("https://www.ajio.com/")
driver.find_element_by_xpath("//input[@name='searchVal']").send_keys("shoes")
driver.find_element_by_xpath("//button[@type='submit']").click()
all_product_names = driver.find_elements_by_xpath("//div[@class='nameCls']")
product_names = [all_product_name.text for all_product_name in all_product_names]
