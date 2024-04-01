import requests
import io
import PIL.Image as Image
import base64
# URL of the Flask login route
captcha_url = 'https://vit-ap-vtop-api-8ae845c27c93.herokuapp.com/getCaptcha'
base64_code = requests.get(captcha_url).text
if base64_code != None:
    captcha_img_binary = base64.b64decode(base64_code)
    img = Image.open(io.BytesIO(captcha_img_binary))
    img.show()
else:
    print("captcha not found!")
captcha=input("Cap : ").upper
# User data (replace with actual user input)
user_data = {
    'username': '23BCE7625',
    'password': '@t6echafuweCo',
    'captcha' : captcha
}
login_url='https://vit-ap-vtop-api-8ae845c27c93.herokuapp.com/login'
# Send POST request with user data as form data
response = requests.post(login_url, data=user_data)
print(response.content)
# Check if request was successful and print response
if response.status_code == 200:
    print('Login successful!')
    print(response.json())
else:
    print('Login failed.')
