from mara_classified.seleniumwrapper import SeleniumWrapper
from mara_classified._excel import read_login_locator
class LoginPage(SeleniumWrapper):
    # _txt_email =("id","email")
    # _txt_password=("id","password")
    # _txt_btn = ("id","loginBtn")
    locators_login = read_login_locator("login")

    def __init__(self,driver):
        super().__init__(driver)

    def login_email(self,email):
        self.enter_element(self.locators_login['_txt_email'],value=email)

    def login_password(self,password):
        self.enter_element(self.locators_login['_txt_password'],value=password)

    def login_button(self):
        self.click_element(self.locators_login['_txt_btn'])