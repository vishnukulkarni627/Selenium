# Without importing the @fixture
def test_login_(_driver):
    _driver.get("https://www.google.com/")
    _driver.find_element_by_xpath('//input[@title="Search"]').send_keys("facebook")
    _driver.quit()