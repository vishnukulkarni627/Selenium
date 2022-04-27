from selenium.webdriver import Chrome
from selenium_wrapper import SeleniumWrapper
def test_registration():
    driver = Chrome("chromedriver.exe")
    driver.get("http://demowebshop.tricentis.com/")
    s = SeleniumWrapper(driver)
    s.click_element(("link text", "Register"))
    s.click_element(("id", "gender-male"))
    s.enter_text(("id", "FirstName"), value = "hello")
    s.enter_text(("id", "LastName"), value = "hai")
    s.enter_text(("id", "Email"), value = "hello.123@gmail.com")
    s.enter_text(("id", "Password"), value = "Password12")
    s.enter_text(("id", "ConfirmPassword"), value = "Password12")
    s.click_element(("id", "register-button"))
    driver.close()