from .constants import PROFILE_URL, HEADERS
from .tools import extract_pfp_base64
from .mentor_details import mentor_details
from .hod_details import hod_details
from .grade_history import get_grade_history
import time
from bs4 import BeautifulSoup

def stu_profile(session,username,csrf_token):
      data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
      html=(session.post(PROFILE_URL,data=data,headers=HEADERS).text)
      soup = BeautifulSoup(html, "html.parser")
      user_data = soup.find_all('td')

      # Define a dictionary to store selected fields
      profile_data = {
        "pfp" : extract_pfp_base64(html),
        "mentor_details" : mentor_details(session,username,csrf_token),
        "hod_and_dean_info" : hod_details(session,username,csrf_token),
        "grade_history" : get_grade_history(session,username,csrf_token)
      }

      # Iterate through user_data and extract selected fields
      for i in range(len(user_data)):
            text = user_data[i].get_text().strip()
            if text == "APPLICATION NUMBER":
                  profile_data["application_number"] = user_data[i+1].get_text().strip()
            elif text == "STUDENT NAME":
                  profile_data["student_name"] = user_data[i+1].get_text().strip()
            elif text == "DATE OF BIRTH":
                  profile_data["dob"] = user_data[i+1].get_text().strip()
            elif text == "GENDER":
                  profile_data["gender"] = user_data[i+1].get_text().strip()
            elif text == "BLOOD GROUP":
                  profile_data["blood_group"] = user_data[i+1].get_text().strip()
            elif text == "EMAIL":
                  profile_data["email"] = user_data[i+1].get_text().strip()

      return profile_data
