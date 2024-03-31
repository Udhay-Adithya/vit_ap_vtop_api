from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route('/')     
def hello_world():
    return 'Hello World'

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username and password:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login Failed'})
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=5000)
