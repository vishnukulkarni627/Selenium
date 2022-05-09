from selenium.webdriver import Chrome
from pytest import fixture

@fixture
def _driver():
    driver = Chrome("./chromedriver.exe")
    driver.get("http://demowebshop.tricentis.com/")
    yield driver
    driver.close()