# from time import sleep
# from selenium.common.exceptions import NoSuchElementException
# def is_login_success(email):
#     _xpath = f"//a[.='{email}']"
#     for _ in range(10):
#         try:
#             if driver.find_element_by_xpath(_xpath).is_displayed():
#                 return True
#             sleep(1)
#             continue
#         except NoSuchElementException:
#             sleep(1)
#             continue
#     return False

# def is_login_auth_error(error_message):
#     _xpath = f"//span[.='{error_message}']"
#     for _ in range(10):
#         try:
#             if driver.find_element_by_xpath(_xpath).is_displayed()
#                 return True
#             sleep(1)
#             continue
#         except NoSuchElementException:
#             sleep(1)
#             continue
#     return False
