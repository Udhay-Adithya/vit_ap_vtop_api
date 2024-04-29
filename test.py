import requests
import io
import PIL.Image as Image
import base64


# Retrieve the API key
API_KEY = 'testing-api-key'  # Replace 'your-api-key' with your actual API key



# Define user data including captcha input
user_data = {
        'username': '',
        'password': '',
    }

    # Define the URL of the Flask login route
url = 'https://vit-ap-vtop-api.vercel.app/login/getAllData'

    # Send POST request with user data and API key in headers
response = requests.post(url, data=user_data,headers={'API_KEY' : API_KEY})
    # Check if request was successful and print response
if response.status_code == 200:
        print('Successful!')
        print(response.text)
else:
        print('Login failed.')
        print(response.text)