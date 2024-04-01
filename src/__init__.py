
'''

from .login import *
import requests
from .user_profile import stu_profile
from .mentor_details import mentor_details
from .biometric_log import get_biometric
from .exam_schedule import exam_schedule
from .time_table import get_time_table
from .captcha import fetch_and_display_captcha
import os
from .constants import *
def main(username,password):
    session = requests.Session()
    if session:
        pre_login(session)
        if fetch_and_display_captcha(session):
            captcha_value = input("Enter the displayed Captcha: ")
            login(session,username, password, captcha_value)
            csrf_token=find_csrf(session.get(VTOP_CONTENT_URL).text)
            # Check if the file exists and delete it
            if os.path.exists("stu_profile.json"):
                os.remove("stu_profile.json")
            if os.path.exists("mentor_details.json"):
                os.remove("mentor_details.json")
            stu_profile(session,username,csrf_token)
            mentor_details(session,username,csrf_token)
            get_biometric(session,username,csrf_token)
            exam_schedule(session=session,username=username,csrf_token=csrf_token,semesterSubId="AP2023247")
            get_time_table(session,username,csrf_token)
if __name__ == "__main__":
    main()

'''