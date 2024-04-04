import os
import sys
import requests
from flask import Flask, request, jsonify
from .login import login
from .captcha import fetch_and_display_captcha
from .prelogin import pre_login,fetch_csrf_token

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

session = requests.Session()

app = Flask(__name__)

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

@app.route('/getCaptcha')     
def captcha():
    global csrf_token
    csrf_token = fetch_csrf_token(session)
    if csrf_token:
        pre_login(session, csrf_token)
        return fetch_and_display_captcha(session)


@app.route('/login', methods=['POST'])
def login_route():
    username = request.form.get('username')
    password = request.form.get('password')
    captcha = request.form.get('captcha')
    return login(session, csrf_token, username, password, captcha)
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=port)
