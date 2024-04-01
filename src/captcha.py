import requests
from .constants import VTOP_URL, VTOP_LOGIN_URL,VTOP_PRELOGIN_URL, USER_AGENT
from .tools import find_captcha,find_csrf

MAX_RETRIES=3
session = requests.Session()
def fetch_and_display_captcha(session, retries=MAX_RETRIES):
    try:
        csrf_token = find_csrf(session.get(VTOP_URL, headers=USER_AGENT).text)
        data = {'_csrf': csrf_token, 'flag': 'VTOP'}
        response = session.post(VTOP_PRELOGIN_URL, data=data, headers=USER_AGENT)
        response.raise_for_status()
        if response.ok:
            print("Pre-login successful")
        else:
            print("Pre-login failed")
    except requests.RequestException as e:
        print("Pre-login request failed:", e)
    
    try:
        html = session.get(VTOP_LOGIN_URL, headers=USER_AGENT).text
        base64_code = find_captcha(html)
        print(base64_code)
        if base64_code:
            return base64_code
        else:
            return None
    except requests.RequestException as e:
        print("Failed to fetch captcha:", e)