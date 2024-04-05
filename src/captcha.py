import requests
from .constants import VTOP_LOGIN_URL, HEADERS
from .tools import find_captcha

MAX_RETRIES=5
def fetch_and_display_captcha(session, retries=MAX_RETRIES):
    """
    Fetches CSRF token from the VTOP website and performs pre-login request.

    Args:
        session (requests.Session): Session object for making HTTP requests.
        retries (int): Number of retries for fetching captcha.

    Returns:
        str or False: Base64 encoded captcha image or False if not found.
    """
    try:
        html = session.get(VTOP_LOGIN_URL, headers=HEADERS).text
        base64_code = find_captcha(html)
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
        return False