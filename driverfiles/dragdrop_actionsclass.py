from selenium.webdriver import Chrome, ActionChains

driver = Chrome("./chromedriver.exe")
driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
a = ActionChains(driver)
src = driver.find_element_by_id("draggable")
dst = driver.find_element_by_id("droppable")
a.drag_and_drop(src,dst).perform()
