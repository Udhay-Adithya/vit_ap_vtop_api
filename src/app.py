import os
import sys

from .session_manager import requests_session

from flask import Flask, jsonify, make_response, request, send_from_directory

from .captcha_solver import fetch_and_display_captcha
from .prelogin import pre_login, fetch_csrf_token
from .profile import stu_profile
from .timetable import get_timetable
from .attendance import get_attendance
from .biometric_log import get_biometric
from .exam_schedule import get_exam_schedule
from .payments import get_payments
from .ncgpa_rank import ncgpa_rank_details
from .handle_login import handle_login
from .weekend_outing import post_weekend_outing_form, get_weekend_outing_response
from .general_outing import post_general_outing_form, get_general_outing_response
from .marks import get_marks

# Adding the project directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = 15 * 60
app.config["SESSION_TYPE"] = "filesystem"


# Retrieve the API key from an environment variable
API_KEY = os.environ.get("API_KEY")


# Middleware to validate API key
def validate_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("API-KEY")
        if api_key != API_KEY:
            return jsonify({"error": "Invalid API key"}), 401
        return func(*args, **kwargs)

    return wrapper


# Apply API key validation middleware to relevant routes
@app.before_request
@validate_api_key
def check_api_key():
    pass


@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")


@app.route("/")
def default_route():
    return ""


@app.route("/helloworld")
def helloworld_route():
    return "Hello World"


@app.route("/getcaptcha", methods=["GET"])
def captcha_route():
    csrf_token = fetch_csrf_token(requests_session)
    if csrf_token:
        pre_login(requests_session, csrf_token)
        return fetch_and_display_captcha(requests_session)


@app.route("/login/getalldata", methods=["POST"])
@handle_login
def new_login_route(
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
):
    return make_response(
        jsonify(
            {
                "profile": stu_profile(requests_session, username, CSRF_TOKEN),
                "attendance": get_attendance(
                    requests_session, username, semSubID, CSRF_TOKEN
                ),
                "timetable": get_timetable(
                    requests_session, username, semSubID, CSRF_TOKEN
                ),
                "exam_schedule": get_exam_schedule(
                    requests_session, username, semSubID, CSRF_TOKEN
                ),
            }
        ),
        200,
    )


@app.route("/login/profile", methods=["POST"])
@handle_login
def profile_route(
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
):
    return make_response(
        jsonify({"profile": stu_profile(requests_session, username, CSRF_TOKEN)}), 200
    )


@app.route("/login/timetable", methods=["POST"])
@handle_login
def time_table_route(
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
):
    return make_response(
        jsonify(
            {
                "timetable": get_timetable(
                    requests_session, username, semSubID, CSRF_TOKEN
                )
            }
        ),
        200,
    )


@app.route("/login/attendance", methods=["POST"])
@handle_login
def attendance_route(
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
):
    return make_response(
        jsonify(
            {
                "attendance": get_attendance(
                    requests_session, username, semSubID, CSRF_TOKEN
                )
            }
        ),
        200,
    )


@app.route("/login/marks", methods=["POST"])
@handle_login
def marks_route(
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
):
    return make_response(
        jsonify({"marks": get_marks(requests_session, username, semSubID, CSRF_TOKEN)}),
        200,
    )


@app.route("/login/examschedule", methods=["POST"])
@handle_login
def examschedule_route(
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
):
    return make_response(
        jsonify(
            {
                "exam_schedule": get_exam_schedule(
                    requests_session, username, semSubID, CSRF_TOKEN
                )
            }
        ),
        200,
    )


@app.route("/login/biometric", methods=["POST"])
@handle_login
def biometric_route(
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
):
    return make_response(
        jsonify(
            {
                "biometric_log": get_biometric(
                    requests_session, username, date, CSRF_TOKEN
                )
            }
        ),
        200,
    )


@app.route("/login/payments", methods=["POST"])
@handle_login
def payment_receipts_route(
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
):
    return make_response(
        jsonify(
            {"payments": get_payments(requests_session, username, applno, CSRF_TOKEN)}
        ),
        200,
    )


@app.route("/login/ncgparankdetails", methods=["POST"])
@handle_login
def ncgparankdetails(
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
):
    return make_response(
        jsonify(
            {
                "ncgpa_rank_details": ncgpa_rank_details(
                    requests_session, username, CSRF_TOKEN
                )
            }
        ),
        200,
    )


@app.route("/login/weekendoutingform", methods=["POST"])
@handle_login
def weekendoutingform(
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
):
    return make_response(
        jsonify(
            {
                "weekend_outing": post_weekend_outing_form(
                    requests_session,
                    username,
                    CSRF_TOKEN,
                    outPlace,
                    purposeOfVisit,
                    outingDate,
                    outTime,
                    contactNumber,
                )
            }
        ),
        200,
    )


@app.route("/login/generaloutingform", methods=["POST"])
@handle_login
def generaloutingform(
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
):
    return make_response(
        jsonify(
            {
                "general_outing": post_general_outing_form(
                    requests_session,
                    username,
                    CSRF_TOKEN,
                    outPlace,
                    purposeOfVisit,
                    outingDate,
                    outTime,
                    inDate,
                    inTime,
                )
            }
        ),
        200,
    )


@app.route("/login/generaloutingrequests", methods=["POST"])
@handle_login
def generaloutingrequests(
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
):
    return make_response(
        jsonify(
            {
                "booking_requests": get_general_outing_response(
                    requests_session, username, CSRF_TOKEN
                )
            }
        ),
        200,
    )


@app.route("/login/weekendoutingrequests", methods=["POST"])
@handle_login
def weekendoutingrequests(
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
):
    return make_response(
        jsonify(
            {
                "booking_requests": get_weekend_outing_response(
                    requests_session, username, CSRF_TOKEN
                )
            }
        ),
        200,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
