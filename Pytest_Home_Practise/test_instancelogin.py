from selenium.webdriver import Chrome
from pytest import fixture
@fixture
def _driver():
    driver = Chrome(r"C:\Users\vishn\PycharmProjects\pythontestingrs\driverfiles\chromedriver.exe")
    driver.get("https://www.google.com")
    return driver

def test_login_(_driver):
    _driver.find_element_by_xpath('//input[@title="Search"]').send_keys("facebook")
    _driver.quit()


