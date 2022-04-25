from selenium.webdriver import Chrome
from pytest import fixture
from time import sleep
@fixture
def _driver():
    print("Launching the Browser Now in _driver Method")
    driver = Chrome(r"C:\Users\vishn\PycharmProjects\pythontestingrs\driverfiles\chromedriver.exe")
    # driver.get("http://demowebshop.tricentis.com/")
    yield driver
    print("Closing the browser in the _driver Method")
    driver.quit()