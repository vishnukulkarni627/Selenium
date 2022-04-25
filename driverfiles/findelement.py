from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select
# /session
# link for search engine
# //button[@title='Search with Google or enter address']/div[.='Search with Google or enter address']
driver = Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/vishn/Downloads/demo-html/demo.html")
# Findelement if no element are matched then returns No such element exception
# Findelements if no element are matched then returns empty list
# elements = driver.find_element_by_name("download")
# to get the text -- text method/property
# to click on webelement -- click()
# to enter the data to the element found --send_keys()
# to get the attribute value then use --- get_attribute()
#  To fetch all the links in a webpage or a specified url
# link = driver.find_elements_by_xpath("//a")
# for links in link:
#     link_text = links.text
#     if "Python" in link_text:
#         print(link_text)
#         sleep(1)
# # Using get attribute we can get the respective values
# element = driver.find_element_by_name("a")
# attributes = ['type','class','id','autocomplete','value','name']
# for i in attributes:
#     print(element.get_attribute(i))

element = driver.find_element_by_id("standard_cars")
s = Select(element)
# The most commonly used is select_by_visible_text
s.select_by_visible_text("Mercedes")
# s.select_by_visible_text("Audi")
# s.select_by_visible_text("Toyota")
# s.select_by_index(7)
# s.select_by_index(10)
# s.select_by_index(3)
# s.select_by_value("bmw")
# s.select_by_value("nin")
#  options returns the list of options from the standard_cars
#  All options are web element
# item= s.options # returns all the options
# data =[] #or #data =[items.text for items in item] #Using list comprehension
# for items in item:
#     print(items.text) # gives the text of each webelement
#     data.append(items.text)
# print(data)
# # or
# for index, item in enumerate(data):
#     if items == "Mercedes":
#         s.select_by_visible_text(items)
#         print(f"the index of {item} is {index}")
#
# #  first_selected_option # returns the currently selected option option: webelement
# s.first_selected_option.text
# #  Mercedes
#
# # in order to select multiple options we have to go with  call this method :select_by_visible_text multiple times
# element = driver.find_element_by_id("multiple_cars")
# s = Select(element)
# # The most commonly used is select_by_visible_text
# s.select_by_visible_text("Mercedes")
# s.select_by_visible_text("Audi")
# s.select_by_visible_text("Toyota")
# s.select_by_index(7)
# s.select_by_index(10)
# s.select_by_index(3)
# s.select_by_value("bmw")
# s.select_by_value("nin")
# # or
# cars = ['Audi', 'Mercedes']
# for car in cars:
#     s.select_by_visible_text(car)
#
# #  Deslecting the option
# s.deselect_by_visible_text("Audi")
# s.deselect_by_value("nin")
# s.deselect_by_index(3)
# s.deselect_all()
#
# #  Selecting all options no direct method is present
# data = [items.text for items in item]
# for items in data:
#     s.select_by_visible_text(items)
#
# # creating a function select_all
# def select_all(list_box):
#     s = Select(list_box)
#     item = s.options
# data = [items.text for items in item]
# for items in data:
#     s.select_by_visible_text(items)
#
# # all_selected_option   - returns all selected options in a list
# s.all_selected_options
# for items in item:
#     print(item.text)