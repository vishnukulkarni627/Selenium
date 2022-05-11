from time import sleep
from requests import request
from selenium.webdriver import Chrome

driver = Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/links.html")
links = driver.find_elements_by_xpath("//a")
urls =[]
broken_links=[]
for link in links:
    urls.append((link.text, link.get_attribute("href")))
for url in urls:
    response = request("GET",url[1])
    if response.status_code !=200:
        # print(f"The link {url} is broken")
        # sleep(1)
        broken_links.append(url)

with open('broken_link.txt','w') as f:
    for item in broken_links:
        f.write(":".join(item))
        f.write("\n")