from Pom_design_pattern_Practice._exc import read
from Pom_design_pattern_Practice.selenium_methods import SeleniumWrapper


class LoginPage(SeleniumWrapper):
    locators = read("login")

    def __init__(self,driver):
        super().__init__(driver)

    def login_enter_email(self,email):
        self.enter_keys(self.locators['_txt_email'],value=email)

    def login_enter_password(self,password):
        self.enter_keys(self.locators['_txt_password'],value=password)

    def login_button(self):
        self.click_element(self.locators['_txt_loginbutton'])
