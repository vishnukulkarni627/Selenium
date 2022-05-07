from selenium.webdriver import Chrome
from selenium_wrapper import SeleniumWrapper
from pytest import mark
from pytestTy._excel import read_locators
from pom_design_pattern.homepage import Homepage
from pom_design_pattern.registration_page import RegistrationPage
from pytestTy._excel import headers, data
# headers = "gender, fname, lname, email, password, conpassword"
# data = [
#     ("Male", "vishnu", "kulkarni", "vishnu.kulkarni@gmail.com","visu123", "visu123"),
#     ("female", "honey", "kulkarni", "honey.kulkarni@gmail.com","honey123", "honey123")
# ]
headers_=headers("smoke", "test_registration")
data_=data("smoke", "test_registration")
@mark.parametrize(headers_, data_)
def test_registration(_driver, gender, fname, lname, email, password, conpassword):
    # driver = Chrome("chromedriver.exe")
    # driver.get("http://demowebshop.tricentis.com/")
    # s = SeleniumWrapper(_driver)
    # s.click_element(("link text", "Register"))
    hp = Homepage(_driver)
    hp.home_click_register()
    rp = RegistrationPage(_driver)
    if gender == "Male":
        rp.reg_select_male()
        # s.click_element(("id", "gender-male"))
    elif gender == "female":
        # s.click_element(("id", "gender-female"))
        rp.reg_select_female()
    else:
        raise Exception("Unknown Gender")

    # s.enter_text(("id", "FirstName"), value = fname)
    rp.reg_enter_fname(fname)
    # s.enter_text(("id", "LastName"), value = lname)
    rp.reg_enter_lname(lname)
    # s.enter_text(("id", "Email"), value = email)
    rp.reg_enter_email(email)
    # s.enter_text(("id", "Password"), value = password)
    rp.reg_enter_password(password)
    # s.enter_text(("id", "ConfirmPassword"), value = conpassword)
    rp.reg_enter_conpassword(conpassword)
    # s.click_element(("id", "register-button"))
    rp.reg_register()
    # driver.close()