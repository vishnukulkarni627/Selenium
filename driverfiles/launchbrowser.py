from selenium.webdriver import Chrome
from time import sleep
# /session
driver = Chrome("./chromedriver.exe")
sleep(2)
# /session/{session id}/url -- post request from postman
driver.get("http://demowebshop.tricentis.com/")
sleep(2)
# /session/{session id}/window/maximize -- post request from postman
driver.maximize_window()
sleep(2)
# /session/{session id}/window/minimize - post request from postman
driver.minimize_window()
sleep(2)
# /session/{session id}/title -- get request from postman
current_title = driver.title
sleep(2)
print(current_title)
# /session/{session id}/url - -get request from postman
current_url= driver.current_url
sleep(2)
print(current_url)
sleep(2)
# /session/{session id}/window -- delete request from postman
driver.close()
