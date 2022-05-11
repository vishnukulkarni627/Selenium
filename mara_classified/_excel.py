import xlrd
def read_login_locator(sheetname):
    locator = {}
    wb = xlrd.open_workbook("./locatordata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    for i in range(1,rows_count):
        rows = ws.row_values(i)
        print(rows)
        locator[rows[0]] = (rows[1],rows[2])
    return locator
# print(read_login_locator("login"))

def read_signup_locator(sheetname):
    locator = {}
    wb = xlrd.open_workbook("./locatordata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count= ws.nrows
    for i in range(1,rows_count):
        rows = ws.row_values(i)
        locator[rows[0]]= (rows[1],rows[2])
    return locator
# print(read_signup_locator("signup"))

def read_headers_login(sheetname, testcase):
    wb = xlrd.open_workbook("./locatordata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    for i in range(0, rows_count):
        rows = ws.row_values(i)
        if rows[0] == testcase:
            headers = ws.row_values(i-1)
            headers = [header for header in headers if header]
            return ",".join(headers[2:])


# print(read_headers_login("login_", "test_login"))

def read_headers_signup(sheetname, testcase):
    wb = xlrd.open_workbook("./locatordata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    for i in range(0, rows_count):
        rows = ws.row_values(i)
        if rows[0] == testcase:
            headers = ws.row_values(i-1)
            headers = [header for header in headers if header]
            return ",".join(headers[2:])
# print(read_headers_signup("login_","test_signup"))

def read_data_login(sheetname,testcase):
    final_data = []
    wb = xlrd.open_workbook("./locatordata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    for i in range(0, rows_count):
        rows = ws.row_values(i)
        if rows[0] == testcase:
            if rows[1].upper() == "YES":
                datas = ws.row_values(i)
                datas = [data for data in datas if data]
                final_data.append(tuple(datas[2:]))
    return final_data
# print(read_data_login("login_", "test_login"))

def read_data_signup(sheetname, testcase):
    final_data=[]
    wb = xlrd.open_workbook("./locatordata.xls")
    ws = wb.sheet_by_name(sheetname)
    rows_count = ws.nrows
    for i in range(0, rows_count):
        rows = ws.row_values(i)
        if rows[0] == testcase:
            if rows[1].upper() == "YES":
                datas = ws.row_values(i)
                datas = [data for data in datas if data]
                datas = datas[1:]
                final_data.append(tuple(datas[1:]))
    return final_data
print(read_data_signup("login_","test_signup"))
