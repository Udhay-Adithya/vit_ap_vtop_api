from flask import Flask, request, jsonify

app = Flask(__name__)

def login(username, password):
    # Your login logic here
    if username == "23BCE7625" and password == "@t6echafuweCo":
        return True
    else:
        return False

@app.route('/login', methods=['POST'])
def login_route():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username and password:
        success = login(username, password)
        if success:
            return jsonify({'success': True, 'message': 'Login successful'})
        else:
            return jsonify({'success': False, 'message': 'Invalid username or password'})
    else:
        return jsonify({'success': False, 'message': 'Username or password not provided'})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
