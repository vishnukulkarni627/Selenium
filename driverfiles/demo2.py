from time import sleep

from selenium.webdriver import Chrome
driver = Chrome("../pytestTy/chromedriver.exe")
items = ['AAPL', 'AA', 'MSFT']
while True:
    for item in items:
        price = driver.find_element_by_xpath(f"//td[.='{item}']/..//td[@class='price']").text
        print(price, end="\t")
    print()
    sleep(0.1)