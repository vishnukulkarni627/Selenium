from Pom_design_pattern_Practice.selenium_methods import SeleniumWrapper
from pytest import mark
from Pom_design_pattern_Practice.homepage_methods import Homepage
from Pom_design_pattern_Practice.registration_pom import Registration
headers = "gender, firstname, lastname, email, password, conpassword"
data = [
    ("Male", "vishnu", "kulkarni", "vishnukulkarni@gmail.com", "visu@123", "visu@123"),
    ("female", "honey", "kulkarni", "honeykulkarni@gmail.com", "honey@123", "honey@123")
]

@mark.parametrize(headers, data)
def test_registration(setup,gender,firstname,lastname,email,password,conpassword):
    hp= Homepage(setup)
    hp.home_click_register()
    rp = Registration(setup)
    if gender == "Male":
        rp.reg_select_male()
    elif gender == "female":
        rp.reg_select_female()
    else:
        raise Exception('Unknown Gender')
    rp.reg_enter_fname(firstname)
    rp.reg_enter_lname(lastname)
    rp.reg_enter_email(email)
    rp.reg_enter_password(password)
    rp.reg_enter_conpassword(conpassword)
    rp.reg_register_button()