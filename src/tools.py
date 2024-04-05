import re
from bs4 import BeautifulSoup


#Find any user error if occurs during login
def login_error_identifier(html):
    soup = BeautifulSoup(html,'html.parser')
    err_msg=soup.find('strong')
    return err_msg.text


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