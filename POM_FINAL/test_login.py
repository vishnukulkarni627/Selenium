from POM_FINAL.seleniumwrapper import SeleniumWrapper
from pytest import mark
from POM_FINAL._excel import read_headers_login,read_data_login
from POM_FINAL.homepage import Homepage
from POM_FINAL.login import LoginPage
headers = read_headers_login("smoke", "test_login_Positive")
data = read_data_login("smoke", "test_login_Positive")
@mark.parametrize(headers, data)
def test_login_Positive(_driver,email,password):
    hp = Homepage(_driver)
    hp.home_click_login()
    lp = LoginPage(_driver)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_button()
