from login import *
import requests
from user_profile import my_profile


def main():
    session = requests.Session()
    csrf_token = fetch_csrf_token(session)
    if csrf_token:
        pre_login(session, csrf_token)
        if fetch_and_display_captcha(session):
            username = '23MIC7175'
            password = 'Shannu0810'
            captcha_value = input("Enter the displayed Captcha: ")
            login(session, csrf_token, username, password, captcha_value)
            my_profile(session,username)
if __name__ == "__main__":
    main()
