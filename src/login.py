from flask import jsonify,make_response
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
            'captchaStr': captcha_value
        }
        response = session.post(VTOP_LOGIN_URL, data=data, headers=HEADERS)
        if response.url == VTOP_CONTENT_URL:
                message=f'Loged in Successfully as {username}'
                return make_response(jsonify({'message': message}), response.status_code)
            
        elif(response.url == VTOP_LOGIN_ERROR_URL):
            error_message = f"Login failed: {login_error_identifier(response.text)}"
            return make_response(jsonify({'message': error_message}), response.status_code)
        
        else:
            return make_response(jsonify({'message': f"Login failed: HTTP status code {response.status_code}"}), response.status_code)
    except requests.RequestException as e:
        print("Login request failed:", e)
        message="Login request failed: Network Error"
        return make_response(jsonify({'message': message}), response.status_code)