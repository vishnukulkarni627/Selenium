from pytest import mark
from mara_classified.homepage import Homepage
from mara_classified.login import LoginPage
headers = "email, password"
data = [
    ("vishnukulkarni61@gmail.com", "visu@1205")
]
@mark.parametrize(headers, data)
def test_login(setup,email,password):
    hp = Homepage(setup)
    hp.home_login_button()
    lp = LoginPage(setup)
    lp.login_email(email)
    lp.login_password(password)
    lp.login_button()
