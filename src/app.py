import os
import sys
import requests
from flask import Flask, request, jsonify
from .login import login
from .captcha import fetch_and_display_captcha

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

session = requests.Session()

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "You can acces this api on Github"

@app.route('/getCaptcha')     
def captcha():
    return fetch_and_display_captcha(session)

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    username = request.form.get('username')
    password = request.form.get('password')
    captcha = request.form.get('captcha')
    if username and password and captcha:
        login(session,username,password,captcha,)
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login Failed'})
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=5000)
