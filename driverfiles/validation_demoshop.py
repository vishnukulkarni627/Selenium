import csv

from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
sleep(2)
# virtual_gift_card=driver.find_element_by_xpath("(//span[@class='price actual-price'])[1]").text
# print(virtual_gift_card)
# We are just extracting the text of the price but we r not extracting with respect to corresponding
# Item
# In order to overcome this issue we use dependent and independent traversing
# write xpath for independent , traverse to parent of both dependent and independent and
# #  attach the dependent xpath
# v_g_c = driver.find_element_by_xpath("//a[.='$25 Virtual Gift Card']/../..//span[@class='price actual-price']").text
# print(v_g_c)
# c_computer = driver.find_element_by_xpath("//a[.='Build your own cheap computer']/../..//span[@class='price actual-price']").text
# print(c_computer)

excepted_prices = {
    "Build your own cheap computer": 800.00,
    "$25 Virtual Gift Card": 25.00,
    "14.1-inch Laptop":1590.00,
    "Simple Computer":800.00
}
for product, excepted_price in excepted_prices.items():
    actual_price = driver.find_element_by_xpath(f"//a[.='{product}']/../..//span[@class='price actual-price']").text
    if excepted_price == float(actual_price):
        print('PASS')
    else:
        print(f"The excepted price of {product}is {excepted_price} but the actual displayed is{actual_price}")

# def csv_():
#     with open(r"C:\Users\vishn\PycharmProjects\pythontestingrs\driverfiles\print.csv") as file:
#         rows = csv.reader(file)
#         headers = next(rows)
#         # for row in rows:
#         #     print(row)
#         excepted_pricess = {row[0]: float(row[1]) for row in rows}
#     return excepted_pricess
#
# if c_computer == csv_:
#     print("pass")