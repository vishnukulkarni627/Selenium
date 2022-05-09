# '# from selenium.webdriver import Chrome
# driver = Chrome("./chromedriver.exe")
# driver.get("https://ifsc.razorpay.com/SBIN0021764")
import csv

from pytest import mark
from requests import request
from json import loads
headers = "code, expected_branch"
# codes = [
#     ("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
#     ("SBIN0040014", "BASAVANAGUDI"),
#     ("ICIC0000002", "BANGALORE - M G ROAD")
# ]
def read_csv():
    codes = []
    with open('./data.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            codes.append(tuple(row))
        return codes
codes = read_csv()
@mark.parametrize(headers, codes)
def test_bank_ifsc(code, expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"
    # Hit the request and collect the response
    response = request('GET', url)
    # Get the actual json string using a property text
    json_string = response.text
    #Converting the json string into pythin data structure i.e Dict
    data = loads(json_string)
    print(data)
    # Parse the dictionary or do a dictionary look up
    actual_branch = data['BRANCH']
    assert actual_branch == expected_branch

