from selenium.webdriver import Chrome
from mara_classified.config import Config
from pytest import fixture
@fixture
def setup():
    driver = Chrome(Config.CHROMEDRIVERPATH)
    driver.get(Config.URL)
    yield driver
    driver.close()