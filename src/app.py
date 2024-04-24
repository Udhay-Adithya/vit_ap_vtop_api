import os
import sys
import requests
from flask import Flask, request, jsonify
from .login import login
from .captcha import fetch_and_display_captcha
from .prelogin import pre_login,fetch_csrf_token
from .time_table import get_time_table
from .attendence import get_attendence
# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

session = requests.Session()
csrf_token = None


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = 15 * 60
app.config["SESSION_TYPE"] = "filesystem"


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

@app.route('/')
def helloworld():
    return "You can acces this api on Github"


@app.route('/getCaptcha', methods=['GET'])     
def captcha():
    global csrf_token
    csrf_token = fetch_csrf_token(session)
    if csrf_token:
        pre_login(session, csrf_token)
        return fetch_and_display_captcha(session)


@app.route('/login/getAllData', methods=['POST'])
def new_login_route():
    username = request.form.get('username')
    password = request.form.get('password')
    captcha = request.form.get('captcha')
    global csrf_token
    if csrf_token is None:
        return jsonify({'error': 'CSRF token not available'}), 500
    return login(session, csrf_token, username, password, captcha)



@app.route('/login/timeTable', methods=['POST'])
def time_table_route():
    username = request.form.get('username')
    password = request.form.get('password')
    captcha = request.form.get('captcha')
    global csrf_token
    if csrf_token is None:
        return jsonify({'error': 'CSRF token not available'}), 500
    else:
        login_resp=login(session, csrf_token, username, password, captcha)
        if login_resp.status_code==200:
            return {'timetable' : get_time_table(session,username)}
        else:
            print(login_resp)


@app.route('/login/attendence', methods=['POST'])
def attendence_route():
    username = request.form.get('username')
    password = request.form.get('password')
    captcha = request.form.get('captcha')
    global csrf_token
    if csrf_token is None:
        return jsonify({'error': 'CSRF token not available'}), 500
    else:
        login_resp=login(session, csrf_token, username, password, captcha)
        if login_resp.status_code==200:
            return {'timetable' : get_attendence(session,username)}
        else:
            print(login_resp)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=port)
