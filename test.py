import requests

# URL of the Flask login route
login_url = 'https://vit-ap-student-app-e1b44cbcf06e.herokuapp.com/login'

# User data (replace with actual user input)
user_data = {
    'username': '23BCE7625',
    'password': '@t6echafuweCo'
}

# Send POST request with user data as form data
response = requests.post(login_url, data=user_data)
print(response)
# Check if request was successful and print response
if response.status_code == 200:
    print('Login successful!')
    print(response.json())
else:
    print('Login failed.')
