from constants import *
from tools import find_csrf
import time
import json
from bs4 import BeautifulSoup
from datetime import datetime,timezone

def exam_schedule(session,username,csrf_token):
    data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
    session.post(EXAM_SCHEDULE_URL,data=data,headers=USER_AGENT)
    data={'authorizedID':username,
          'semesterSubId':'AP2023247',
          '_csrf':csrf_token
          }
    html=session.post(GET_EXAM_SCHEDULE_URL,data=data,headers=USER_AGENT).text
    soup = BeautifulSoup(html, "html.parser")
    user_data = soup.find_all('td')
    for i in user_data:
        with open('exam_schedule.json', 'a') as json_file:
            json.dump(user_data, json_file, indent=4)