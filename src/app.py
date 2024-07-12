import os
import sys
import requests
from flask import Flask,request, jsonify
from .constants import VTOP_CONTENT_URL,HEADERS
from .login import login
from .captcha_solver import fetch_and_display_captcha,solve_captcha
from .prelogin import pre_login,fetch_csrf_token,find_csrf
from .user_profile import stu_profile
from .timetable import get_timetable
from .attendence import get_attendence
from .biometric_log import get_biometric
from .exam_schedule import get_exam_schedule
from .payment_receipts import get_payment_receipts
from .ncgpa_rank import ncgpa_rank_details



# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
requests_session = requests.Session()



app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = 15 * 60
app.config["SESSION_TYPE"] = "filesystem"


'''
# Retrieve the API key from an environment variable
API_KEY = os.environ.get('API_KEY')

# Middleware to validate API key
def validate_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('API-Key')
        if api_key != API_KEY:
            return jsonify({'error': 'Invalid API key'}), 401
        return func(*args, **kwargs)
    return wrapper

# Apply API key validation middleware to relevant routes
@app.before_request
@validate_api_key
def check_api_key():
    pass
'''


@app.route('/')
def default_route():
    return ""


@app.route('/helloworld')
def helloworld_route():
    return "Hello World"


@app.route('/getcaptcha', methods=['GET'])
def captcha():
    csrf_token = fetch_csrf_token(requests_session)
    if csrf_token:
        pre_login(requests_session, csrf_token)
        return fetch_and_display_captcha(requests_session)


@app.route('/login/getalldata', methods=['POST'])
def new_login_route():
    username = request.form.get('username')
    password = request.form.get('password')
    semSubID = request.form.get('semSubID')
    csrf_token = fetch_csrf_token(requests_session)
    pre_login(requests_session, csrf_token)   
    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
    login_resp=login(requests_session, csrf_token, username, password, captcha)
    if login_resp.status_code==200:
        CSRF_TOKEN = find_csrf(requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text)
        return {'profile': stu_profile(requests_session,username,CSRF_TOKEN),
                'attendence' : get_attendence(requests_session,username,semSubID,CSRF_TOKEN),
                'timetable':get_timetable(requests_session,username,semSubID,CSRF_TOKEN),
                'exam_schedule' : get_exam_schedule(requests_session,username,semSubID,CSRF_TOKEN)}
    else:
        return login_resp


@app.route('/login/profile', methods=['POST'])
def profile_route():
    username = request.form.get('username')
    password = request.form.get('password')
    csrf_token = fetch_csrf_token(requests_session)
    pre_login(requests_session, csrf_token)   
    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
    login_resp=login(requests_session, csrf_token, username, password, captcha)
    if login_resp.status_code==200:
        CSRF_TOKEN = find_csrf(requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text)
        return {'profile': stu_profile(requests_session,username,CSRF_TOKEN)}
    else:
        return login_resp
    


@app.route('/login/timetable', methods=['POST'])
def time_table_route():
    username = request.form.get('username')
    password = request.form.get('password')
    semSubID = request.form.get('semSubID')
    csrf_token = fetch_csrf_token(requests_session)
    pre_login(requests_session, csrf_token)
    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
    login_resp=login(requests_session, csrf_token, username, password, captcha)
    if login_resp.status_code==200:
        CSRF_TOKEN = find_csrf(requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text)
        return {'timetable':get_timetable(requests_session,username,semSubID,CSRF_TOKEN)}
    else:
        return login_resp


@app.route('/login/attendence', methods=['POST'])
def attendence_route():
    username = request.form.get('username')
    password = request.form.get('password')
    semSubID = request.form.get('semSubID')
    csrf_token = fetch_csrf_token(requests_session)
    pre_login(requests_session, csrf_token)   
    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
    login_resp=login(requests_session, csrf_token, username, password, captcha)
    if login_resp.status_code==200:
        CSRF_TOKEN = find_csrf(requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text)
        return {'attendence' : get_attendence(requests_session,username,semSubID,CSRF_TOKEN)}
    else:
        return login_resp



@app.route('/login/examschedule', methods=['POST'])
def examschedule_route():
    username = request.form.get('username')
    password = request.form.get('password')
    semSubID = request.form.get('semSubID')
    csrf_token = fetch_csrf_token(requests_session)
    pre_login(requests_session, csrf_token)   
    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
    login_resp=login(requests_session, csrf_token, username, password, captcha)
    if login_resp.status_code==200:
        CSRF_TOKEN = find_csrf(requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text)
        return {'exam_schedule' : get_exam_schedule(requests_session,username,semSubID,CSRF_TOKEN)}
    else:
        return login_resp
    

@app.route('/login/biometric', methods=['POST'])
def biometric_route():
    username = request.form.get('username')
    password = request.form.get('password')
    date = request.form.get('date')
    csrf_token = fetch_csrf_token(requests_session)
    pre_login(requests_session, csrf_token)   
    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
    login_resp=login(requests_session, csrf_token, username, password, captcha)
    if login_resp.status_code==200:
        CSRF_TOKEN = find_csrf(requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text)
        return {'biometric_log' : get_biometric(requests_session,username,date,CSRF_TOKEN)}
    else:
        return login_resp


@app.route('/login/paymentreceipts', methods=['POST'])
def payment_receipts_route():
    username = request.form.get('username')
    password = request.form.get('password')
    csrf_token = fetch_csrf_token(requests_session)
    pre_login(requests_session, csrf_token)   
    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
    login_resp=login(requests_session, csrf_token, username, password, captcha)
    if login_resp.status_code==200:
        CSRF_TOKEN = find_csrf(requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text)
        return {'payment_receipts' : get_payment_receipts(requests_session,username,CSRF_TOKEN)}
    else:
        return login_resp


@app.route('/login/ncgparankdetails', methods=['POST'])
def ncgparankdetails():
    username = request.form.get('username')
    password = request.form.get('password')
    csrf_token = fetch_csrf_token(requests_session)
    pre_login(requests_session, csrf_token)   
    captcha = solve_captcha(fetch_and_display_captcha(requests_session))
    login_resp=login(requests_session, csrf_token, username, password, captcha)
    if login_resp.status_code==200:
        CSRF_TOKEN = find_csrf(requests_session.get(VTOP_CONTENT_URL, headers=HEADERS).text)
        return {'ncgpa_rank_details' : ncgpa_rank_details(requests_session,username,CSRF_TOKEN)}
    else:
        return login_resp

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=port)
