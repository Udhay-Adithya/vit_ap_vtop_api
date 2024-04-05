import requests
from .constants import VTOP_LOGIN_URL, VTOP_CONTENT_URL, VTOP_LOGIN_ERROR_URL, HEADERS
from .tools import login_error_identifier

def login(session, csrf_token, username, password, captcha_value):
    """
    Attempts to log in to the VTOP system using provided credentials.

    Args:
        session (requests.Session): Session object for making HTTP requests.
        csrf_token (str): Cross-Site Request Forgery token required for the login request.
        username (str): Username for logging in.
        password (str): Password for logging in.
        captcha_value (str): Value of the CAPTCHA image for validation.

    Returns:
        str: A string indicating the outcome of the login attempt.
             - If login is successful, returns "Login Successful".
             - If login fails due to an internal error, returns "Login failed due to some internal Error".
             - If login fails due to other reasons, returns an error message describing the issue.

    Raises:
        None

    """

    try:
        data = {
            '_csrf': csrf_token,
            'username': username,
            'password': password,
            'captchaStr': captcha_value.upper()  # Ensure captcha is in uppercase
        }
        response = session.post(VTOP_LOGIN_URL, data=data, headers=HEADERS)
        if response.status_code == 200:
            if response.url == VTOP_CONTENT_URL:
                return f'Loged in Successfully as {username}'
            
        elif(response.url == VTOP_LOGIN_ERROR_URL):
            error_message = login_error_identifier(response.text)
            
            return f"Login failed: {error_message}"
        else:
            return f"Login failed: HTTP status code {response.status_code}"
    except requests.RequestException as e:
        print("Login request failed:", e)
        return "Login request failed: Network Error"