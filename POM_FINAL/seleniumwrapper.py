from selenium.webdriver.support.select import Select

from wait_mechanism import wait
class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver
    @wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()
    @wait
    def enter_element(self,locator,*, value):
        self.driver.find_element(*locator).send_keys(value)
    # def select_item(self, locator, *, item):
    #     element = self.driver.find_element(*locator)
    #     s = Select(element)
    #     if isinstance(s, str):


