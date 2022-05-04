import xlrd
def read_locators(sheetname):
    wb = xlrd.open_workbook("./data.xls")
    ws = wb.sheet_by_name(sheetname)
    rows = ws.get_rows()
    # for row in rows:
    #     print(row)
        # print(row[0].value, row[1].value, row[2].value)
    headers = next(rows)
    locators = {row[0].value : (row[1].value, row[2].value) for row in rows}
    return locators


# read_locators("login")

