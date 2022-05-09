from requests import request
from pytest import mark
from json import loads
def test_success_register():
    url = "https://reqres/api/register"

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = request("POST", url, json= payload)

    assert response.status_code == 200

    json_string = response.text

    py_obj =  loads(json_string)
    is_token_present = 'token' in py_obj
    assert is_token_present == True

def test_failpwd_register():
    url = "https://reqres/api/register"

    payload = {
        "email": "eve.holt@reqres.in",

    }

    response = request("POST", url, json= payload)

    assert response.status_code == 400


def test_failmail_register():
    url = "https://reqres/api/register"

    payload = {
        "password": "pistol",

    }

    response = request("POST", url, json=payload)

    assert response.status_code == 400
