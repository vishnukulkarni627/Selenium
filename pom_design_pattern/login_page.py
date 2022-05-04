from time import sleep
from selenium.common.exceptions import NoSuchElementException
from pytestTy.selenium_wrapper import SeleniumWrapper
from pytestTy._excel import read_locators
class LoginPage(SeleniumWrapper):
    # _txt_email = ("id", "Email")
    # _txt_password = ("id", "Password")
    # _txt_loginbutton = ("xpath", "//input[@value='Log in']")
    locators = read_locators('login')

    def __init__(self, driver):
        super().__init__(driver)
    def login_enter_email(self, email):
        # self.enter_text(self._txt_email, value=email)
        self.enter_text(self.locators['_txt_email'], value=email)
    def login_enter_password(self,password):
        # self.enter_text(self._txt_password, value=password)
        self.enter_text(self.locators['_txt_password'], value=password)
    def login_click_login(self):
        # self.click_element(self._txt_loginbutton)
        self.click_element(self.locators['_txt_loginbutton'])
    def is_login_auth_error(self,error_message):
        _xpath = f"//span[.='{error_message}']"
        for _ in range(10):
            try:
                if self.driver.find_element_by_xpath(_xpath).is_displayed():
                    return True
                sleep(1)
                continue
            except NoSuchElementException:
                sleep(1)
                continue
        return False
