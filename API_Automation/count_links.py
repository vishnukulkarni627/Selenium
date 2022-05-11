import re

from requests import request
import re

def count_links():
    response = request("GET","http://demowebshop.tricentis.com/")
    html_code = response.text
    match = re.findall(r"\s*<a\s+", html_code)
    return len(match)
print(count_links())