from time import sleep
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("https://www.cleartrip.com/flights/")
sleep(2)
driver.maximize_window()
driver.find_element_by_xpath("//input[@placeholder='Any worldwide city or airport']").click()
sleep(2)
places = driver.find_elements_by_xpath("//p[@class='to-ellipsis o-hidden ws-nowrap c-inherit fs-3']")
for place in places:
    if place.text == 'Bangalore, IN - Kempegowda International Airport (BLR)':
        _xpath = f"//p[.='{place.text}']"
driver.find_element_by_xpath(_xpath).click()
driver.find_element_by_xpath("(//input[@placeholder='Any worldwide city or airport'])[2]").click()
placesto = driver.find_elements_by_xpath("//p[@class='to-ellipsis o-hidden ws-nowrap c-inherit fs-3']")
for placeto in placesto:
    if placeto.text == 'Kolkata, IN - Netaji Subhas Chandra Bose Airport (CCU)':
        _xpathto = f"//p[.='{placeto.text}']"
driver.find_element_by_xpath(_xpathto).click()

driver.find_element_by_xpath("//div[@class='flex flex-middle flex-between p-relative homeCalender']/button").click()
sleep(5)
_month = 'April 2022'
_day = 29
for _ in range(12):
    try:
        _xpath2 = f"//div[.='{_month}']/../..//div[.='{_day}']"
        driver.find_element_by_xpath(_xpath2).click()

    except NoSuchElementException:
        driver.find_element_by_css_selector('svg[data-testid="rightArrow"]').click()
        sleep(1)
        continue
driver.find_element_by_xpath("//div[@class='col flex flex-middle']/button").click()