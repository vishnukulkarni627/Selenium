from Pom_design_pattern_Practice.wait_mechanism import wait__

class SeleniumWrapper:
    def __init__(self,driver):
        self.driver= driver
    @wait__
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
    @wait__
    def enter_keys(self,locator, *, value):
        self.driver.find_element(*locator).send_keys(value)


