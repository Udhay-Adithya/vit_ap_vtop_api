import requests

# Define your Flask app as usual
from flask import Flask

app = Flask(__name__)

# Define a route to trigger sending test username and password
@app.route('/send_credentials')
def send_credentials():
    # Define the test username and password
    test_username = '23BCE7625'
    test_password = 'Adithya@123'

    # Send a POST request with the test credentials
    response = requests.post('https://vit-ap-student-app-e1b44cbcf06e.herokuapp.com/', json={'username': test_username, 'password': test_password})

    # Check the response from the server
    if response.status_code == 200:
        return 'Test credentials sent successfully'
    else:
        return 'Failed to send test credentials'

if __name__ == '__main__':
    app.run(debug=True)