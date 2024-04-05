from .constants import PROFILE_URL, HEADERS
import time
import json
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
        "APPLICATION_NUMBER": "",
        "STUDENT_NAME": "",
        "DATE_OF_BIRTH": "",
        "GENDER": "",
        "BLOOD_GROUP": "",
        "EMAIL": ""
      }

      # Iterate through user_data and extract selected fields
      for i in range(len(user_data)):
            text = user_data[i].get_text().strip()
            if text == "APPLICATION NUMBER":
                  profile_data["APPLICATION_NUMBER"] = user_data[i+1].get_text().strip()
            elif text == "STUDENT NAME":
                  profile_data["STUDENT_NAME"] = user_data[i+1].get_text().strip()
            elif text == "DATE OF BIRTH":
                  profile_data["DATE_OF_BIRTH"] = user_data[i+1].get_text().strip()
            elif text == "GENDER":
                  profile_data["GENDER"] = user_data[i+1].get_text().strip()
            elif text == "BLOOD GROUP":
                  profile_data["BLOOD_GROUP"] = user_data[i+1].get_text().strip()
            elif text == "EMAIL":
                  profile_data["EMAIL"] = user_data[i+1].get_text().strip()

      # Write the selected fields to a JSON file
      with open("stu_profile.json", 'w') as f:
            json.dump(profile_data, f, indent=2)
