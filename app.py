from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login_route():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username and password:
        return jsonify({'success': True, 'message': 'Login successful'})
if __name__ == '__main__':
    app.run(debug=True,port=5000)
