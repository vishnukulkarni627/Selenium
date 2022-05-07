from Pom_design_pattern_Practice.selenium_methods import SeleniumWrapper
from Pom_design_pattern_Practice._exc import read
class Registration(SeleniumWrapper):
    locators = read("Registration")


    def __init__(self,driver):
        super().__init__(driver)

    def reg_select_male(self):
        self.click_element(self.locators['_rdo_male'])
    def reg_select_female(self):
        self.click_element(self.locators['_rdo_female'])
    def reg_enter_fname(self,firstname):
        self.enter_keys(self.locators['_txt_fname'], value=firstname)
    def reg_enter_lname(self,lastname):
        self.enter_keys(self.locators['_txt_lname'], value=lastname)
    def reg_enter_email(self,email):
        self.enter_keys(self.locators['_txt_email'], value = email)
    def reg_enter_password(self,password):
        self.enter_keys(self.locators['_txt_password'], value= password)
    def reg_enter_conpassword(self,conpassword):
        self.enter_keys(self.locators['_txt_conpassword'], value= conpassword)
    def reg_register_button(self):
        self.click_element(self.locators['_txt_registerbutton'])

