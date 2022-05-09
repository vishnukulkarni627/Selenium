from time import sleep
from requests import request
from selenium.webdriver import Chrome

driver = Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/links.html")
links = driver.find_elements_by_xpath("//a")
urls =[]
for link in links:
    urls.append(link.get_attribute("href"))
for url in urls:
    response = request("GET",url)
    if response.status_code !=200:
        print(f"The link {url} is broken")
        sleep(1)