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
    accessing the wrapped route. It now includes a retry mechanism for 
    handling temporary login failures.

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
        Wrapper function that executes the login process with retry logic.

        Returns:
        --------
        Response
            A Flask HTTP response indicating either successful login and
            execution of the wrapped function or an error message.
        """

        IS_VTOP_DOWN = False
        MAX_RETRIES = 3  # Maximum number of login retry attempts
        
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
        receitNo = request.form.get("receitNo")

        if IS_VTOP_DOWN != True:
            if len(username) > 5:
                if not any(
                    char in set(string.punctuation + string.whitespace)
                    for char in username
                ):
                    # Retry loop for login
                    for attempt in range(MAX_RETRIES):
                        try:
                            # Fetch fresh CSRF token for each retry
                            csrf_token = fetch_csrf_token(requests_session)
                            
                            # Perform pre-login steps
                            pre_login(requests_session, csrf_token)
                            
                            # Solve captcha
                            captcha = solve_captcha(fetch_and_display_captcha(requests_session))
                            
                            # Attempt login
                            login_resp = login(
                                requests_session, csrf_token, username, password, captcha
                            )
                            
                            # Check login response
                            if login_resp.status_code == 200:
                                # Successful login
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
                                    receitNo,
                                    *args,
                                    **kwargs
                                )
                            
                            # Handle 404 status with retry
                            elif login_resp.status_code == 404:
                                # Log the retry attempt if logging is implemented
                                # logging.warning(f"Login attempt {attempt + 1} failed. Retrying...")
                                print(f"Login attempt {attempt + 1} failed. Retrying...")
                                continue
                            
                            # Other status codes indicate a different type of error
                            else:
                                return make_response(
                                    jsonify({"error": login_resp.json}),
                                    login_resp.status_code,
                                )
                        
                        except Exception as e:
                            # Handle any unexpected errors during login process
                            return make_response(
                                jsonify({"error": {"login": f"Login error: {str(e)}"}}),
                                500
                            )
                    
                    # If all retry attempts fail
                    return make_response(
                        jsonify({"error": {"login": "Failed to login after multiple attempts"}}),
                        404
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