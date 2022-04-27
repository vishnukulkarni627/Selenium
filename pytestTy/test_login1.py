from selenium.webdriver import Chrome
from selenium_wrapper import SeleniumWrapper
def test_login(_driver):
    # driver = Chrome("chromedriver.exe")
    # driver.get("http://demowebshop.tricentis.com/")
    s = SeleniumWrapper(_driver)
    s.click_element(("link text", "Log in"))
    s.enter_text(("id", "Email"), value = "bill.gates@company.com")
    s.enter_text(("id", "Password"), value = "Password12")
    s.click_element(("xpath", "//input[@value='Log in']"))
    # driver.close()