import re


#Find csrf token
def find_csrf(html):
    #Search for the csrfValue using the regular expression
    pattern = r'<input type="hidden" name="_csrf" value="([0-9a-f-]+)"'
    return re.search(pattern, html).group(1)

#Find base64 code of captcha
def find_captcha(html):
    pattern = r'data:image/jpeg;base64,([^"]+)'
    return re.search(pattern, html).group(1)