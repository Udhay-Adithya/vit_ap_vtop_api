import requests
from .constants import VTOP_URL,HEADERS,VTOP_PRELOGIN_URL
from .tools import find_csrf



def fetch_csrf_token(session):
    """
    Fetches CSRF token from the VTOP website.

    Args:
        session (requests.Session): Session object for making HTTP requests.

    Returns:
        str or None: CSRF token if found, None otherwise.
    """
    try:
        response = session.get(VTOP_URL, headers=HEADERS).text
        csrf_token = find_csrf(response)
        if csrf_token is not None:
            print("Found CSRF token")
            return csrf_token
        else:
            print("CSRF token not found")
            fetch_csrf_token(session)
    except requests.RequestException as e:
        print("Failed to fetch CSRF token:", e)
        return None
    

def pre_login(session, csrf_token):
    """
    Sends pre-login request to VTOP website.

    Args:
        session (requests.Session): Session object for making HTTP requests.
        csrf_token (str): CSRF token to be included in the request.

    Returns:
        None
    """
    try:
        data = {'_csrf': csrf_token, 'flag': 'VTOP'}
        response = session.post(VTOP_PRELOGIN_URL, data=data, headers=HEADERS)
        if response.ok:
            print("Pre-login successful")
        else:
            print("Pre-login failed")
    except requests.RequestException as e:
        print("Pre-login request failed:", e)