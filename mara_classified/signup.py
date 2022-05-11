from mara_classified._excel import read_signup_locator
from mara_classified.seleniumwrapper import SeleniumWrapper
class Signup(SeleniumWrapper):
    # _select_gender = ("id", "gender")
    # # _select_mr = ("xpath", "//ul[@class='select2-results__options']//li[contains(text(),'{Gender}')]")
    # # _select_mrs = ("xpath", "//ul[@class='select2-results__options']//li[contains(text(),'{Gender}')]")
    # _txt_name = ("name","name")
    # _rdo_pro = ("id","user_type-2")
    # _rdo_bus = ("id","user_type-3")
    # _select_country =("id","country")
    # _txt_phone=("name","phone")
    # _txt_email=("id","email")
    # _txt_password=("id","password")
    # _txt_conpass = ("id","password_confirmation")
    # _chk_box = ("id","term")
    # _reg_btn= ("id","signup_btn")
    locator_signup = read_signup_locator("signup")
    def __init__(self,driver):
        super().__init__(driver)

    def sel_gender_male(self,Gender):
        self.select_item(self.locator_signup['_select_gender'], item=Gender)

    def sel_gender_female(self,Gender):
        self.select_item(self.locator_signup['_select_gender'], item=Gender)

    def reg_enter_name(self,Name):
        self.enter_element(self.locator_signup['_txt_name'], value=Name)

    def reg_select_pro(self):
        self.click_element(self.locator_signup['_rdo_pro'])

    def reg_select_bus(self):
        self.click_element(self.locator_signup['_rdo_bus'])

    def sel_country(self,Your_country):
        self.select_item(self.locator_signup['_select_country'],item=Your_country)

    def reg_enter_phone(self,phone):
        self.enter_element(self.locator_signup['_txt_phone'], value=phone)

    def reg_enter_email(self,email):
        self.enter_element(self.locator_signup['_txt_email'], value=email)

    def reg_enter_password(self,password):
        self.enter_element(self.locator_signup['_txt_password'], value=password)

    def reg_enter_conpass(self,conpass):
        self.enter_element(self.locator_signup['_txt_conpass'], value=conpass)

    def chk_box(self):
        self.click_element(self.locator_signup['_chk_box'])

    def reg_btn(self):
        self.click_element(self.locator_signup['_reg_btn'])