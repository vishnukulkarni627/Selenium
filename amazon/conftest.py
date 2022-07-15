import pytest
from selenium.webdriver import Chrome
@pytest.fixture
def setup():
    driver = Chrome("./chromedriver.exe")
    driver.get("https://www.amazon.in")
    yield driver
    driver.close()
