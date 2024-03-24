from login import *
import requests
from user_profile import stu_profile
from mentor_details import mentor_details
import os
from constants import *
def main():
    session = requests.Session()
    login_csrf_token = fetch_csrf_token(session)
    if login_csrf_token:
        pre_login(session, login_csrf_token)
        if fetch_and_display_captcha(session):
            username = '23BCE7930'
            password = 'Vicky12345'
            captcha_value = input("Enter the displayed Captcha: ")
            login(session, login_csrf_token, username, password, captcha_value)
            csrf_token=find_csrf(session.get(VTOP_CONTENT_URL).text)
            # Check if the file exists and delete it
            if os.path.exists("stu_profile.json"):
                os.remove("stu_profile.json")
            if os.path.exists("mentor_details.json"):
                os.remove("mentor_details.json")
            stu_profile(session,username,csrf_token)
            mentor_details(session,username,csrf_token)
if __name__ == "__main__":
    main()
