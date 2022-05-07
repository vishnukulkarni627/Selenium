from Pom_design_pattern_Practice.homepage_methods import Homepage
from pytest import mark
from Pom_design_pattern_Practice.selenium_methods import SeleniumWrapper
from Pom_design_pattern_Practice.login_pom import LoginPage
headers = "email ,password"
data = [
    ("bill.gates@company.com","Password123"),
    ("hello.world@company.com", "Password123")
]
@mark.parametrize(headers, data)
def test_login_positive(setup,email,password):
    hp = Homepage(setup)
    hp.home_click_login()
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_button()
