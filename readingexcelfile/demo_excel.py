import xlrd

def read_excel(sheetname):
    workbook = xlrd.open_workbook("./demo.xls")
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    headers = next(rows)
    return {row[0].value: (row[1].value, row[2].value) for row in rows}


print(read_excel("name"))
