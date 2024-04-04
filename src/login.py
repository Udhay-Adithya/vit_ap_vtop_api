import requests
from .constants import VTOP_LOGIN_URL, HEADERS


def login(session, csrf_token, username, password, captcha_value):
    print("Logingn in....")
    try:
        data = {
            '_csrf': csrf_token,
            'username': username,
            'password': password,
            'captchaStr': captcha_value.upper()  # Ensure captcha is in uppercase
        }
        response = session.post(VTOP_LOGIN_URL, data=data, headers=HEADERS)
        return response.text
    except requests.RequestException as e:
        print("Login request failed:", e)