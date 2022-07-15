from classified_utlities.homepage import Homepage
from classified_utlities.signup import Signup
from pytest import mark
from classified_utlities._excel import read_headers_signup, read_data_signup
# headers = "Gender, Name, You_are_a, Your_country, phone, email, password, conpass"
headers_signup = read_headers_signup("login_","test_signup")
# data = [
#     ("Mr", "vishnu", "Professional", "India", "1234568846", "vishnukulkarni1@gmail.com", "visu@1205", "visu@1205"),
#     ("Mrs", "honey", "Individual", "India", "5465845465", "vishnukulkarni2@gmail.com", "visu@212", "visu@212")
# ]
data_signup = read_data_signup("login_", "test_signup")
@mark.parametrize(headers_signup, data_signup)
def test_signup(setup,Gender,Name,You_are_a,Your_country,phone,email,password,conpass):
    hp = Homepage(setup)
    hp.home_signup_button()
    sp = Signup(setup)
    if Gender == 'Mr':
        sp.sel_gender_male('Mr')
    elif Gender == 'Mrs':
        sp.sel_gender_female('Mrs')
    else:
        raise Exception('Unknown Gender')
    sp.reg_enter_name(Name)
    if You_are_a == 'Professional':
        sp.reg_select_pro()
    elif You_are_a == 'Individual':
        sp.reg_select_bus()
    else:
        raise Exception("Not Found")
    if Your_country == 'India':
        sp.sel_country('India')
    else:
        raise Exception("Enter India Only")
    sp.reg_enter_phone(phone)
    sp.reg_enter_email(email)
    sp.reg_enter_password(password)
    sp.reg_enter_conpass(conpass)
    sp.chk_box()
    sp.reg_btn()


