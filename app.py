from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Get the data from the request body in JSON format
    data = request.json

    # Extract the username and password from the JSON data
    username = data.get('username')
    password = data.get('password')

    # Now you can use the username and password variables as needed

    # For example, you can return a response indicating successful login
    response = {'message': 'Login successful', 'username': username}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)