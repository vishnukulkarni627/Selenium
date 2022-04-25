from time import sleep

from selenium.webdriver import Chrome
driver = Chrome("./chromedriver.exe")
driver.get('http://demowebshop.tricentis.com/')
links = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")

for link in links:
    print(link.text)
    sleep(0.5)

links_footer = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
for link_footer in links_footer:
    print(link_footer.text)
    sleep(0.3)