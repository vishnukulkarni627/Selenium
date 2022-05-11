from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert

driver = Chrome("../pytestTy/chromedriver.exe")
driver.maximize_window()
driver.get('https://www.monsterindia.com/')
sleep(2)
# driver.find_element_by_xpath("//button[@class='No thanks']").click()
# sleep(5)
driver.find_element_by_xpath("//input[@class='input search-bar home_ac']").send_keys("python")
sleep(2)
driver.find_element_by_xpath("//div[@class='home_ac']//strong[.='Python']").click()
sleep(3)
driver.find_element_by_xpath("//div[@class='col-xl-2 col-lg-3 col-sm-2 col-xxs-12 fl no-padding']/input[@class='btn']").click()
sleep(5)
# job_titles = driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")
# for job_title in job_titles:
#     print(job_title.text)
#     sleep(0.1)
driver.find_element_by_xpath("//div[@class='job-tittle']/h3/a").click()
ids = driver.window_handles
driver.switch_to.window(ids[1])
sleep(5)
driver.find_element_by_xpath("//div[@class='col-sm-8 col-xxs-7 ssa-wrap-mt10 ']//button").click()