import csv

from pytest import mark
from requests import request
from json import loads
url = "https://reqres.in/api/users?page=2"
response = request("GET", url)

# validate status code
assert response.status_code ==200
json_string = response.text
py_obj = loads(json_string)

users = py_obj['data']
with open("./user.csv", "w") as f:
    writer = csv.DictWriter(f, ["id","email","first_name","last_name","avatar"])
    writer.writeheader()
    for user in users:
        writer.writerow(user)
        # print(user['id'], user['email'], user['first_name'], user['last_name'], user['avatar'])
