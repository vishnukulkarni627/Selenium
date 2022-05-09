from POM_FINAL.seleniumwrapper import SeleniumWrapper
from POM_FINAL._excel import read_homelocator
class Homepage(SeleniumWrapper):
    # _lnk_login = ("link text", "Log in")
    # _lnk_register = ("link text", "Register")
    locator = read_homelocator("homepage")
    def __init__(self, driver):
        super().__init__(driver)
    def home_click_login(self):
        self.click_element(self.locator['_lnk_login'])
    def home_click_register(self):
        self.click_element(self.locator['_lnk_register'])