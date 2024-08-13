import string
from flask import request, jsonify, make_response, Response
from functools import wraps
from .session_manager import requests_session
from .constants import VTOP_CONTENT_URL, HEADERS
from .login import login
from .captcha_solver import fetch_and_display_captcha, solve_captcha
from .prelogin import pre_login, fetch_csrf_token, find_csrf


def handle_login(func):
    """
    Decorator function to handle VTOP login authentication for a Flask route.

    This decorator ensures that a user is authenticated with VTOP before
    accessing the wrapped route. It performs several tasks:

    - Checks if the VTOP service is down.
    - Validates the provided username.
    - Fetches and solves a captcha for the login process.
    - Performs a login request to VTOP.
    - Retrieves a CSRF token for further requests after login.
    - Passes the required arguments (like username, CSRF token, etc.) to the
      wrapped function upon successful login.

    Parameters:
    -----------
    func : function
        The Flask route handler function to be wrapped and executed after
        successful authentication.

    Returns:
    --------
    function
        The wrapper function that manages the login flow and then calls the
        original route handler if authentication is successful.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that executes the login process and, upon success,
        calls the wrapped route handler.

        This function handles:
        - Validation of the username.
        - Execution of the pre-login and login processes.
        - Retrieval of a CSRF token after successful login.
        - Passing the necessary arguments to the wrapped function.

        Returns:
        --------
        Response
            A Flask HTTP response indicating either successful login and
            execution of the wrapped function or an error message.
        """

        IS_VTOP_DOWN = False
        username = request.form.get("username")
        password = request.form.get("password")
        semSubID = request.form.get("semSubID")
        applno = request.form.get("applno")
        date = request.form.get("date")
        outPlace = request.form.get("outPlace")
        purposeOfVisit = request.form.get("purposeOfVisit")
        outingDate = request.form.get("outingDate")
        outTime = request.form.get("outTime")
        inDate = request.form.get("inDate")
        inTime = request.form.get("inTime")
        contactNumber = request.form.get("contactNumber")
        if IS_VTOP_DOWN != True:
            if len(username) > 5:
                if not any(
                    char in set(string.punctuation + string.whitespace)
                    for char in username
                ):
                    csrf_token = fetch_csrf_token(requests_session)
                    pre_login(requests_session, csrf_token)
                    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
                    login_resp = login(
                        requests_session, csrf_token, username, password, captcha
                    )
                    if login_resp.status_code == 200:
                        CSRF_TOKEN = find_csrf.find_csrf(
                            requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text
                        )
                        return func(
                            username,
                            semSubID,
                            date,
                            applno,
                            outPlace,
                            purposeOfVisit,
                            outingDate,
                            outTime,
                            inDate,
                            inTime,
                            contactNumber,
                            CSRF_TOKEN,
                            *args,
                            **kwargs
                        )
                    else:
                        return make_response(
                            jsonify({"error": login_resp.data}), login_resp.status_code
                        )
                else:
                    return make_response(
                        jsonify(
                            {"error": {"login": "Username contains special characters"}}
                        ),
                        404,
                    )
            else:
                return make_response(
                    jsonify({"error": {"login": "Username too short"}}),
                    404,
                )
        else:
            return make_response(
                jsonify({"error": {"login": "Seems like VTOP is down"}}), 404
            )

    return wrapper
