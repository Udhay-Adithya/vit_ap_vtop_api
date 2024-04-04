import requests
from .constants import VTOP_LOGIN_URL, HEADERS
from .tools import find_captcha

MAX_RETRIES=3
session = requests.Session()
def fetch_and_display_captcha(session, retries=MAX_RETRIES):

    try:
        html = session.get(VTOP_LOGIN_URL, headers=HEADERS).text
        base64_code = find_captcha(html)
        print(base64_code)
        if base64_code != 'Null':
            return base64_code
        elif retries > 0:
                print(f"Retrying... {retries} retries left.")
                return fetch_and_display_captcha(session, retries - 1)
        else:
                print("Maximum retries reached. Captcha not found.")
                return None
    except requests.RequestException as e:
        print("Failed to fetch captcha:", e)
        if retries > 0:
            print(f"Retrying... {retries} attempts left.")
            return fetch_and_display_captcha(session, retries=retries-1)
        else:
            print("Maximum retries reached. Aborting.")
            return False