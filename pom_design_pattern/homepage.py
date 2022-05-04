from time import sleep
from selenium.common.exceptions import NoSuchElementException
from pytestTy.selenium_wrapper import SeleniumWrapper
class Homepage(SeleniumWrapper):
    _lnk_register = ("link text", "Register")
    _lnk_login = ("link text", "Log in")
    def __init__(self,driver):
        super().__init__(driver)
    def home_click_register(self):
        self.click_element(self._lnk_register)
    def home_click_login(self):
        self.click_element(self._lnk_login)

    def is_login_success(self,email):
        _xpath = f"//a[.='{email}']"
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