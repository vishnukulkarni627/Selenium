from classified_utlities.seleniumwrapper import SeleniumWrapper
class Homepage(SeleniumWrapper):
    _lnk_signup = ("link text", "Signup")
    _lnk_login = ("link text", "Login")

    def __init__(self,driver):
        super().__init__(driver)

    def home_signup_button(self):
        self.click_element(self._lnk_signup)

    def home_login_button(self):
        self.click_element(self._lnk_login)
