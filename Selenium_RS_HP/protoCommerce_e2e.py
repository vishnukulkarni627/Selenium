from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome("./chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//a[.='Shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    p_name = product.find_element_by_xpath("div/h4/a").text
    print(p_name)
    if p_name == "Blackberry":
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
success_text = (driver.find_element_by_class_name("alert-success").text)
assert "Success! Thank you!" in success_text
driver.save_screenshot("defect.png")