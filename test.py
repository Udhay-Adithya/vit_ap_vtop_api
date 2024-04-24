import requests
import io
import PIL.Image as Image
import base64

# Define the URL of the Flask login route
captcha_url = 'https://vit-ap-vtop-api-8ae845c27c93.herokuapp.com/getCaptcha'

# Retrieve the API key
API_KEY = 'test-api-key'  # Replace 'your-api-key' with your actual API key

# Send GET request to fetch captcha image and handle response
captcha_response = requests.get(captcha_url,headers={'API-Key': API_KEY})

if captcha_response.status_code == 200:
    # Decode the base64 encoded image
    captcha_img_binary = base64.b64decode(captcha_response.text)
    
    # Display the captcha image
    img = Image.open(io.BytesIO(captcha_img_binary))
    img.show()
    
    # Get user input for captcha
    captcha_input = input("Enter Captcha: ").upper()

    # Define user data including captcha input
    user_data = {
        'username': '23BCE7930',
        'password': 'Vicky12345',
        'captcha': captcha_input
    }

    # Define the URL of the Flask login route
    url = 'https://vit-ap-vtop-api-8ae845c27c93.herokuapp.com/login/attendence'

    # Send POST request with user data and API key in headers
    response = requests.post(url, data=user_data, headers={'API-Key': API_KEY})
    # Check if request was successful and print response
    if response.status_code == 200:
        print('Successful!')
        print(response.text)
    else:
        print('Login failed.')
        print(response.text)
else:
    print('Error',captcha_response.text)
