from json import loads

from pytest import mark
from requests import request

headers = "email, expected_status"
emails = [
    ("hello.world", "failure"),
    ("hello.world@company.com", "success"),
    ("hello.world@", "failure"),
    ("hello.world@.com", "failure"),
    ("hello.world@company.gov.in","success"),
    ("hello.world@company.edu", "success")
]

@mark.parametrize(headers, emails)
def test_mail(email, expected_status):
    url = f"https://api.eva.pingutil.com/email?email={email}"
    response = request("GET", url)
    json_string = response.text
    data = loads(json_string)
    actual_status = data['status']

    assert actual_status == expected_status
