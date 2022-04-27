from selenium.webdriver import Chrome
from time import sleep
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/demo.html")
sleep(5)
# driver.find_element_by_link_text("Inbox(100)").click()
#  The part of the link text is dynamically changing, every time we have to change in script
# in order to mitigate this issue, we use partial link text
driver.find_element_by_partial_link_text("Inbox").click()
# But if we have multiple words like shopping it gives a matches for both but results on first matching element
