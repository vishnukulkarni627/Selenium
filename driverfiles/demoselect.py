from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/demo.html")
ele = driver.find_element_by_id("standard_cars")
s = Select(ele)
all_options = s.options
for all_option in all_options:
    print(all_option.text)

# s.select_by_visible_text("Audi")
# s.select_by_visible_text("BMW")
# s.select_by_value("for")
# s.deselect_all()


