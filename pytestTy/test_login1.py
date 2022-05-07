from selenium.webdriver import Chrome
from pytest import mark
from selenium_wrapper import SeleniumWrapper
from pom_design_pattern.login_page import LoginPage
from pytestTy._excel import headers, data
from pom_design_pattern.homepage import Homepage
# from lib import is_login_success
# headers = "email ,password"
# data = [
#     ("bill.gates@company.com","Password123"),
#     ("hello.world@company.com", "Password123")
# ]
headers_=headers("smoke", "test_login_Positive")
data_=data("smoke", "test_login_Positive")

@mark.parametrize(headers_, data_)
def test_login_Positive(_driver, email, password):
    # driver = Chrome("chromedriver.exe")
    # driver.get("http://demowebshop.tricentis.com/")
    # s = SeleniumWrapper(_driver)
    # s.click_element(("link text", "Log in"))
    hp = Homepage(_driver)
    hp.home_click_login()
    lp = LoginPage(_driver)
    # The below three line codes are implemented in Call POM Functions
    # s.enter_text(("id", "Email"), value = email)
    lp.login_enter_email(email)
    # s.enter_text(("id", "Password"), value = password)
    lp.login_enter_password(password)
    # s.click_element(("xpath", "//input[@value='Log in']"))
    lp.login_click_login()

    assert hp.is_login_success(email) == True
#     if is_login_success(email):
#         print("Success")
#     else:
#         print("Fail")
# #     # driver.close()
#
# headers = "email ,password, error_message"
# data = [
#     ("bill.gates@company.com","password12", "Login was unsuccessful. Please correct the errors and try again."),
#     ("hello.com", "password12", "Please enter a valid email address.")
# ]

headers_= headers("smoke", "test_login_Negative")
data_=data("smoke", "test_login_Negative")
#
@mark.parametrize(headers_, data_)
def test_login_Negative(_driver, email, password, error_message):
    # driver = Chrome("chromedriver.exe")
    # driver.get("http://demowebshop.tricentis.com/")
    # s = SeleniumWrapper(_driver)
    # s.click_element(("link text", "Log in"))
    # s.enter_text(("id", "Email"), value = email)
    # s.enter_text(("id", "Password"), value = password)
    # s.click_element(("xpath", "//input[@value='Log in']"))
    hp = Homepage(_driver)
    hp.home_click_login()
    lp = LoginPage(_driver)
    # The below three line codes are implemented in Call POM Functions
    # s.enter_text(("id", "Email"), value = email)
    lp.login_enter_email(email)
    # s.enter_text(("id", "Password"), value = password)
    lp.login_enter_password(password)
    # s.click_element(("xpath", "//input[@value='Log in']"))
    lp.login_click_login()
#
    assert lp.is_login_auth_error(error_message) == True
    # if is_login_auth_error(error_message):
    #     print("Pass")
    # else:
    #     print("Fail")
# # driver.close()