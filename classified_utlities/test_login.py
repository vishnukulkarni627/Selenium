from pytest import mark
from classified_utlities.homepage import Homepage
from classified_utlities.login import LoginPage
from classified_utlities._excel import read_headers_login, read_data_login
# headers = "email, password"
headers_login = read_headers_login("login_","test_login")
# data = [
#     ("vishnukulkarni61@gmail.com", "visu@1205")
# ]
data_login = read_data_login("login_", "test_login")
@mark.parametrize(headers_login, data_login)
def test_login(setup,email,password):
    hp = Homepage(setup)
    hp.home_login_button()
    lp = LoginPage(setup)
    lp.login_email(email)
    lp.login_password(password)
    lp.login_button()
