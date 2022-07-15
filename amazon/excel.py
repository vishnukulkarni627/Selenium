import xlrd
def read_headers_login(sheetname,testcase):
    wb = xlrd.open_workbook("./testdataamazon.xls")
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
    wb = xlrd.open_workbook("./testdataamazon.xls")
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