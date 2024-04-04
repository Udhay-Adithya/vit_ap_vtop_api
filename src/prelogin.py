import requests
from .constants import VTOP_URL,HEADERS,VTOP_PRELOGIN_URL
from .tools import find_csrf



def fetch_csrf_token(session):
    try:
        response = session.get(VTOP_URL, headers=HEADERS).text
        csrf_token = find_csrf(response)
        if csrf_token:
            return csrf_token
        else:
            print("CSRF token not found")
            return None
    except requests.RequestException as e:
        print("Failed to fetch CSRF token:", e)
        return None
    

def pre_login(session, csrf_token):
    try:
        data = {'_csrf': csrf_token, 'flag': 'VTOP'}
        response = session.post(VTOP_PRELOGIN_URL, data=data, headers=HEADERS)
        response.raise_for_status()
        if response.ok:
            print("Pre-login successful")
        else:
            print("Pre-login failed")
    except requests.RequestException as e:
        print("Pre-login request failed:", e)