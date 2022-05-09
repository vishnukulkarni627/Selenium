from POM_FINAL.seleniumwrapper import SeleniumWrapper
from POM_FINAL._excel import read_login_locator
class LoginPage(SeleniumWrapper):
    locator = read_login_locator("login")

    def __init__(self,driver):
        super().__init__(driver)

    def login_enter_email(self,email):
        self.enter_element(self.locator['_txt_email'],value=email)

    def login_enter_password(self,password):
        self.enter_element(self.locator['_txt_password'],value=password)

    def login_button(self):
        self.click_element(self.locator['_txt_loginbutton'])