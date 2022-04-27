from selenium.webdriver import Chrome
driver = Chrome("../pytestTy/chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/demo.html")
fnames = driver.find_elements_by_xpath("//table[@name='customers']//td[2]")
names =[fname.text for fname in fnames]
print(names)
names_sort_= sorted(names)
print(names_sort_)
print(names == names_sort_)
