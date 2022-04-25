from time import sleep

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome('./chromedriver.exe')
driver.get("https://meesho.com/")
act=driver.find_element_by_xpath("//input[@placeholder='Try Saree, Kurti or Search by Product Code']").send_keys("shoes")
a = ActionChains(driver)
a.key_up(Keys.ENTER).perform()
a.key_down(Keys.ENTER).perform()
sleep(5)
driver.find_element_by_xpath("//div[@class='Card__BaseCard-sc-b3n78k-0 dUNFgg NewProductCard__DetailCard_Desktop-sc-j0e7tu-2 fqvaeS NewProductCard__DetailCard_Desktop-sc-j0e7tu-2 fqvaeS']").click()
sleep(5)
sizes = driver.find_elements_by_xpath("//div[@class='Chipsstyled__ChipsWrapper-sc-id03eo-0 kynQFI SizeSelection__SizeSelectorChipsStyled-sc-1yyqfl-2']/span/span")
for size in sizes:
    print(size.text)
    if size.text == "IND-8":
        _xpath= f"//span[.='{size.text}']"
        driver.find_element_by_xpath(_xpath).click()
driver.find_element_by_xpath("//div[@class='Card__BaseCard-sc-b3n78k-0 jzcoqI']").click()



