import requests
from .constants import VTOP_LOGIN_URL, VTOP_CONTENT_URL, VTOP_LOGIN_ERROR_URL, HEADERS
from .utils import find_login_response
from flask import jsonify, Response, make_response


def login(
    session: requests.Session,
    csrf_token: str,
    username: str,
    password: str,
    captcha_value: str,
) -> Response:
    """
    Attempts to log in to the VTOP system using provided credentials.

    Args:
        session (requests.Session): Session object for making HTTP requests.
        csrf_token (str): Cross-Site Request Forgery token required for the login request.
        username (str): Username for logging in.
        password (str): Password for logging in.
        captcha_value (str): Value of the CAPTCHA image for validation.

    Returns:
        Response: A Flask Response object containing a JSON-formatted message indicating the outcome of the login attempt.
            - If login is successful, the JSON will contain "message": "Logged in Successfully as {username}".
            - If login fails due to incorrect credentials or CAPTCHA, the JSON will contain "error": "specific error message".
            - If a network-related issue occurs, the JSON will contain "error": "Login request failed: Network Error".
            - The HTTP status code will reflect the result:
                - 200 if login is successful.
                - 401 if login fails due to incorrect credentials or CAPTCHA.
                - 404 if an unexpected response is received (e.g., redirection to an unknown URL).
                - 503 if a network-related error occurs.

    Raises:
        None
    """
    try:
        data = {
            "_csrf": csrf_token,
            "username": username,
            "password": password,
            "captchaStr": captcha_value,
        }
        response = session.post(VTOP_LOGIN_URL, data=data, headers=HEADERS)
        if response.url == VTOP_CONTENT_URL:
            message = f"Logged in Successfully as {username}"
            return make_response(jsonify({"res": message}), 200)

        elif response.url == VTOP_LOGIN_ERROR_URL:
            error_message = find_login_response.login_error_identifier(response.text)
            return make_response(jsonify({"login": error_message}), 401)

        else:
            return make_response(
                jsonify(
                    {"login": f"Login failed: HTTP status code {response.status_code}"}
                ),
                404,
            )
    except requests.RequestException:
        message = "Login request failed: Network Error"
        return make_response(jsonify({"login": message}), 503)
