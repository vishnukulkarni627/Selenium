from pytest import mark
@mark.parametrize(headers, data)
def test_signin_Positive(setup,email,password):
    hp = Homepage(setup)
    hp.home_click_login()
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_button()