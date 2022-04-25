from selenium.webdriver import Chrome
from time import sleep
driver = Chrome(r"C:\Users\vishn\PycharmProjects\pythontestingrs\driverfiles\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
register = driver.find_element_by_link_text("register")
register.click() #  A session is created with a Id and looks for an element in webpage if not found we get No such element exception
sleep(2)