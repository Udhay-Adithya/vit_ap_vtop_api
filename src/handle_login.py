import string
from flask import request, jsonify, make_response
from functools import wraps
from .session_manager import requests_session
from .constants import VTOP_CONTENT_URL, HEADERS
from .login import login
from .captcha_solver import fetch_and_display_captcha, solve_captcha
from .prelogin import pre_login, fetch_csrf_token, find_csrf


def handle_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
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
        contactNumber = request.form.get("contactNumber")
        if IS_VTOP_DOWN != True:
            if len(username) > 5:
                if (
                    any(
                        char in set(string.punctuation + string.whitespace)
                        for char in username
                    )
                ) == False:
                    csrf_token = fetch_csrf_token(requests_session)
                    pre_login(requests_session, csrf_token)
                    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
                    login_resp, status_code = login(
                        requests_session, csrf_token, username, password, captcha
                    )
                    if status_code == 200:
                        CSRF_TOKEN = find_csrf(
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
                            contactNumber,
                            CSRF_TOKEN,
                            *args,
                            **kwargs
                        )
                    else:
                        return make_response(
                            jsonify({"error": login_resp}), status_code
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
