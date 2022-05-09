import xlrd
#
def read_homelocator(sheetname):
    locators = {}
    wb = xlrd.open_workbook("./data.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    print(rows_count)
    for i in range(1, rows_count):
        rows = ws.row_values(i)
        locators[rows[0]] = (rows[1],rows[2])
    return locators

# print(read_homelocator("homepage")

def read_headers_login(sheetname,testcase):
    wb = xlrd.open_workbook("./testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    for i in range(0, rows_count):
        row= ws.row_values(i)
        if row[0] == testcase:
            headers = ws.row_values(i-1)
            headers = [header for header in headers if header]
            return ",".join(headers[2:])
print(read_headers_login("smoke","test_login_Positive"))

def read_data_login(sheetname,testcase):
    wb = xlrd.open_workbook("./testdata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    final_data = []
    for i in range(0, rows_count):
        row = ws.row_values(i)
        if row[0] == testcase:
            data = ws.row_values(i)
            data = [row for row in data if row]
            data = data[1:]
            if data[0].upper()== "YES":
                final_data.append(tuple(data[1:]))
    return final_data
print(read_data_login("smoke","test_login_Positive"))


def read_login_locator(sheetname):
    locator_login = {}
    wb = xlrd.open_workbook("./data.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    for i in range(1,rows_count):
        row = ws.row_values(i)
        locator_login[row[0]] = (row[1], row[2])
    return locator_login
# print(read_login_locator("login"))