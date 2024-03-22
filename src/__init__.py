from login import *
import requests

def main():
    #Create a new session
    session=requests.Session()
    prelogin(session)
    captcha(session)
    user_captcha=input("Enter the displayed Captcha : ").upper()
    username='23BCE7625'
    password='Adithya@123'
    login(username,password,session,user_captcha)

main()