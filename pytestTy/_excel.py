import itertools
from itertools import chain
import xlrd
# def read_locators(sheetname):
#     wb = xlrd.open_workbook("./data.xls")
#     ws = wb.sheet_by_name(sheetname)
#     rows = ws.get_rows()
#     # for row in rows:
#     #     print(row)
#         # print(row[0].value, row[1].value, row[2].value)
#     headers = next(rows)
#     locators = {row[0].value : (row[1].value, row[2].value) for row in rows}
#     return locators

def read_locators(sheetname):
    wb = xlrd.open_workbook("./data.xls")
    ws = wb.sheet_by_name(sheetname)
    row_count = ws.nrows    #6
    # col_count = ws.ncols    #3
    locators = {}
    for i in range(1, row_count):
        row_data = ws.row_values(i)
        locators[row_data[0]] = (row_data[1], row_data[2])
    return locators
# print(read_locators("login"))

# def headers(sheetname, testcase):
#     wb = xlrd.open_workbook("./testdata.xls")
#     ws = wb.sheet_by_name(sheetname)
#     rows = ws.get_rows()
#     for index, row in enumerate(rows):
#         if row[0].value == testcase:
#             headers_=ws.row_values(index-1, start_colx=2)
#             # Evaluates to boolean value of each item of the list (column)
#             headers_ = [item for item in headers_ if item]
#             return ",".join(headers_)
#
# print(headers("smoke", "test_login"))

def headers(sheetname, testcase):
    wb = xlrd.open_workbook("./testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    row_count = ws.nrows
    for i in range(0, row_count):
        row = ws.row_values(i)
        if row[0] == testcase:
            headers_= ws.row_values(i-1)
            headers_= [header_ for header_ in headers_ if header_]
            return ",".join(headers_[2:])
# print(headers("smoke", "test_registration"))
# def data(sheetname, testcase):
#     email_ = []
#     password_=[]
#     wb = xlrd.open_workbook("./testdata.xls")
#     ws = wb.sheet_by_name(sheetname)
#     rows = ws.get_rows()
#     for index, row in enumerate(rows):
#         if row[0].value == testcase:
#             email= ws.row_values(index, start_colx=2, end_colx=3)
#             # email= [item for item in email if item]
#             for item in email:
#                 email_.append(item)
#             password = ws.row_values(index, start_colx=3, end_colx=4)
#             for item in password:
#                 password_.append(item)
#     data_= list(zip(email_, password_))
#     return data_


# print(data("smoke", "test_login"))

def data(sheetname, testcase):
    wb = xlrd.open_workbook("./testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    row_count = ws.nrows
    final_data =[]
    for i in range(0, row_count):
        row = ws.row_values(i)
        if row[0] == testcase:
            data_= ws.row_values(i)
            # Removing those items with empty string or empty columns
            data_= [row for row in data_ if row]
            # Not interested in test script name, so slicing everything from 1st index
            data_ = data_[1:]
            #Not interested
            if data_[0].upper() == "YES":
                final_data.append(tuple(data_[1:]))
    return final_data

# print(data("smoke", "test_login"))