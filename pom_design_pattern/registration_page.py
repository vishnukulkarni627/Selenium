from pytestTy.selenium_wrapper import SeleniumWrapper
from pytestTy._excel import read_locators
class RegistrationPage(SeleniumWrapper):
    # _rdo_male = ("id", "gender-male")
    # _rdo_female = ("id", "gender-female")
    # _txt_fname = ("id", "FirstName")
    # _txt_lname = ("id", "LastName")
    # _txt_email = ("id", "Email")
    # _txt_password = ("id", "Password")
    # _txt_conpassword = ("id", "ConfirmPassword")
    # _txt_registerbutton = ("id", "register-button")
    locators = read_locators('Registration')
    def __init__(self,driver):
        super().__init__(driver)

    def reg_select_male(self):
        # self.click_element(self._rdo_male)
        self.click_element(self.locators['_rdo_male'])
    def reg_select_female(self):
        # self.click_element(self._rdo_female)
        self.click_element(self.locators['_rdo_female'])
    def reg_enter_fname(self,fname):
        # self.enter_text(self._txt_fname, value=fname)
        self.enter_text(self.locators['_txt_fname'], value=fname)
    def reg_enter_lname(self,lname):
        # self.enter_text(self._txt_lname, value=lname)
        self.enter_text(self.locators['_txt_lname'], value=lname)
    def reg_enter_email(self,email):
        # self.enter_text(self._txt_email, value=email)
        self.enter_text(self.locators['_txt_email'], value=email)
    def reg_enter_password(self,password):
        # self.enter_text(self._txt_password, value=password)
        self.enter_text(self.locators['_txt_password'], value=password)
    def reg_enter_conpassword(self,conpassword):
        # self.enter_text(self._txt_conpassword, value=conpassword)
        self.enter_text(self.locators['_txt_conpassword'], value=conpassword)
    def reg_register(self):
        # self.click_element(self._txt_registerbutton)
        self.click_element(self.locators['_txt_registerbutton'])