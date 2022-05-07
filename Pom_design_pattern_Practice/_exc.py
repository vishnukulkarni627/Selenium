import xlrd

def read(sheetname):
    wb = xlrd.open_workbook("./data.xls")
    ws = wb.sheet_by_name(sheetname)
    rows = ws.get_rows()
    locators = {row[0].value:(row[1].value, row[2].value) for row in rows}
    return locators


