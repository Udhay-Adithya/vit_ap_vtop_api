import requests
import io
import PIL.Image as Image
import base64
# URL of the Flask login route
login_url = 'https://vit-ap-student-app-e1b44cbcf06e.herokuapp.com/getCaptcha'
base64_code = requests.get(login_url)
print(base64_code)
captcha_img_binary = base64.b64decode(base64_code)
img = Image.open(io.BytesIO(captcha_img_binary))
img.show()
# User data (replace with actual user input)
user_data = {
    'username': '23BCE7625',
    'password': '@t6echafuweCo'
}

# Send POST request with user data as form data
response = requests.post(login_url, data=user_data)
print(response.content)
# Check if request was successful and print response
if response.status_code == 200:
    print('Login successful!')
    print(response.json())
else:
    print('Login failed.')
