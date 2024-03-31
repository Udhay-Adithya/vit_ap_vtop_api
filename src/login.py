import requests
from constants import VTOP_URL, VTOP_PRELOGIN_URL, VTOP_LOGIN_URL, USER_AGENT
from tools import find_csrf, find_captcha


def fetch_csrf_token(session):
    try:
        global csrf_token
        csrf_token = find_csrf(session.get(VTOP_URL, headers=USER_AGENT).text)
        if csrf_token:
            return csrf_token
        else:
            print("CSRF token not found")
            return None
    except requests.RequestException as e:
        print("Failed to fetch CSRF token:", e)
        return None


def login(session, username, password, captcha_value):
    try:
        data = {
            '_csrf': csrf_token,
            'username': username,
            'password': password,
            'captchaStr': captcha_value.upper()  # Ensure captcha is in uppercase
        }
        response = session.post(VTOP_LOGIN_URL, data=data, headers=USER_AGENT)
    except requests.RequestException as e:
        print("Login request failed:", e)

    if e :
        return "Login request failed:",e
    else:
        return "Login Successful",response