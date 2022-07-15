from selenium.webdriver import Chrome
# from classified_utlities.config import Config
from pytest import fixture
@fixture
def setup():
    driver = Chrome("./chromedriver.exe")
    driver.get("http://122.166.192.191:9003/")
    yield driver
    driver.close()