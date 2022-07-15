from selenium_wrapper import SeleniumWrapper
class Homepage(SeleniumWrapper):
    _lnk_signin =("link text", "Hello, Sign in")
    _lnk_signup =("link text", "Start here.")
    def __init__(self, driver):
        super().__init__(driver)
    def home_click_signin(self):
        self.click_element(self._lnk_signin)
    def home_click_signup(self):
        self.click_element(self._lnk_signup)

