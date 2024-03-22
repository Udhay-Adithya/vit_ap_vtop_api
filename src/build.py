import requests
import re
from constants import *

# Create a session object
session=requests.Session()
# Make a GET request to VTOP_PRELOGIN_URL to fetch the initial CSRF token
response=session.get(VTOP_URL,headers=USER_AGENT)
# Use regex to extract the CSRF token from the response
pattern = r'<input type="hidden" name="_csrf" value="([0-9a-f-]+)"'
match = re.search(pattern, response.text)

if match:
    csrf_token = match.group(1)
else:
    print("CSRF token not found")
    csrf_token = None

# Make a POST request to VTOP_PRELOGIN_URL with the extracted CSRF token
if csrf_token:
    data = {'_csrf': csrf_token, 'flag': 'VTOP'}
    response = session.post(VTOP_PRELOGIN_URL, data=data, headers=USER_AGENT)

    # Check if the POST request was successful
    if response.ok:
        print("POST request successful")
    else:
        print("POST request failed")

# Make a GET request to VTOP_PRELOGIN_INIT_URL using the same session
#response1 = session.get(VTOP_PRELOGIN_INIT_URL, headers=USER_AGENT)

response2=session.get(VTOP_LOGIN_URL,headers=USER_AGENT)

# Check the response
print(response2.text)