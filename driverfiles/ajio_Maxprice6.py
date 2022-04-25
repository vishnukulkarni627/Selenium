# 1. Open Ajio website and get the first 6 maximum price of shoes along with the product description.
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver = Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get("https://www.ajio.com/")
sleep(5)
driver.find_element_by_xpath("//input[@name='searchVal']").send_keys("shoes")
driver.find_element_by_xpath("//button[@type='submit']").click()
sort_=driver.find_element_by_xpath("//div[@class='filter-dropdown']/..//select")
s = Select(sort_)
s.select_by_visible_text("Price (highest first)")
sleep(5)
products = driver.find_elements_by_xpath("//div[@class='contentHolder']")
count = 0
n = 6
for product in products:
    count +=1
    if count <= n:
        print(product.text)
        print('--------------------------')


# brand = driver.find_element_by_xpath("//div[@class='contentHolder']/..//div[@class = 'brand']").text
# name = driver.find_element_by_xpath("//div[@class='contentHolder']/..//div[@class = 'nameCls']").text
# price = driver.find_element_by_xpath("//div[@class='contentHolder']/..//span[@class='price  ']").text
# offer = driver.find_element_by_xpath("//div[@class='contentHolder']/..//div[@class='offer-div']").text
# print(brand,name,price,offer)