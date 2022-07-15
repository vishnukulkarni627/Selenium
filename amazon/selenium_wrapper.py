from wait import wait
class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver
    @wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()
    @wait
    def enter_element(self,locator,*, value):
        self.driver.find_element(*locator).send_keys(value)