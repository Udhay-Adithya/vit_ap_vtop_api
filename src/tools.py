import re
from urllib.parse import quote


def password_validator(password : str):
    # Encode the input string
    encoded_string = quote(password)
    return encoded_string

#Find csrf token
def find_csrf(html):
    #Search for the csrfValue using the regular expression
    pattern = r'<input type="hidden" name="_csrf" value="([0-9a-f-]+)"'
    return re.search(pattern, html).group(1)

#Find base64 code of captcha
def find_captcha(html):
    pattern = r'data:image/jpeg;base64,([^"]+)'
    match=re.search(pattern, html)
    if match:
        return re.search(pattern, html).group(1)
    else:
        return None