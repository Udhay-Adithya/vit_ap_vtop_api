from login import *
import requests
from user_profile import my_profile
def main():
    #Create a new session
    session=requests.Session()
    prelogin(session)
    captcha(session)
    user_captcha=input("Enter the displayed Captcha : ").upper()
    username='23BCE7625'
    password=password_validator('Adithya@123')
    login(username,password,session,user_captcha)
    #my_profile(session,username)
main()