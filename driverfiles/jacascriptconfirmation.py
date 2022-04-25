from time import sleep
from selenium.webdriver import Chrome
driver = Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/demo.html")
sleep(2)
driver.find_element_by_id("delete").click()
sleep(1)
# driver.switch_to.alert.accept()  # Clicks ok on confirmation
msg = driver.switch_to.alert.text
if msg == "Are You Sure You Want to Delete":
    print("pass")
else:
    print("Fail")
sleep(2)
driver.switch_to.alert.dismiss()    #clicks cancel on confirmation