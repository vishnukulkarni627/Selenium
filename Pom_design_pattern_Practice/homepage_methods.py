from Pom_design_pattern_Practice.selenium_methods import SeleniumWrapper
class Homepage(SeleniumWrapper):
    _lnk_register = ("link text", "Register")
    _lnk_login = ("link text", "Log in")

    def __init__(self,driver):
        super().__init__(driver)

    def home_click_login(self):
        self.click_element(self._lnk_login)

    def home_click_register(self):
        self.click_element(self._lnk_register)
