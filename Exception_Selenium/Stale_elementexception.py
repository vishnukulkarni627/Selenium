from selenium.webdriver import Chrome
from time import sleep
driver = Chrome(r"C:\Users\vishn\PycharmProjects\pythontestingrs\driverfiles\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
register = driver.find_element_by_link_text("Register")
register.click() #  A session is created with a Id
sleep(2)
register.click()   # Here it tries to click on old genereated session id
#Hence we get Stale element exception