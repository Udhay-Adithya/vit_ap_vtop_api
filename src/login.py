import requests
import re
import PIL.Image as Image
import base64
import io
from constants import VTOP_URL, VTOP_PRELOGIN_URL, VTOP_LOGIN_URL, USER_AGENT
from tools import find_csrf, find_captcha

MAX_RETRIES=3

def fetch_csrf_token(session):
    try:
        response = session.get(VTOP_URL, headers=USER_AGENT).text
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
        response = session.post(VTOP_PRELOGIN_URL, data=data, headers=USER_AGENT)
        response.raise_for_status()
        if response.ok:
            print("Pre-login successful")
        else:
            print("Pre-login failed")
    except requests.RequestException as e:
        print("Pre-login request failed:", e)

def fetch_and_display_captcha(session, retries=MAX_RETRIES):
    try:
        html = session.get(VTOP_LOGIN_URL, headers=USER_AGENT).text
        base64_code = find_captcha(html)
        if base64_code:
            captcha_img_binary = base64.b64decode(base64_code)
            img = Image.open(io.BytesIO(captcha_img_binary))
            img.show()
            return True
        elif(base64_code==None):
            print("Failed to fetch captcha.")
            return False
    except requests.RequestException as e:
        print("Failed to fetch captcha:", e)
        if retries > 0:
            print(f"Retrying... {retries} attempts left.")
            return fetch_and_display_captcha(session, retries=retries-1)
        else:
            print("Maximum retries reached. Aborting.")
            return False

def login(session, csrf_token, username, password, captcha_value):
    try:
        data = {
            '_csrf': csrf_token,
            'username': username,
            'password': password,
            'captchaStr': captcha_value.upper()  # Ensure captcha is in uppercase
        }
        response = session.post(VTOP_LOGIN_URL, data=data, headers=USER_AGENT)
        print(response.url)
    except requests.RequestException as e:
        print("Login request failed:", e)