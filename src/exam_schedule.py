from .constants import *
from .tools import find_csrf
import time
import json
from bs4 import BeautifulSoup

def exam_schedule(session,username,csrf_token,semesterSubId):
    data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
    session.post(EXAM_SCHEDULE_URL,data=data,headers=USER_AGENT)
    data={'authorizedID':username,
          'semesterSubId':semesterSubId,
          '_csrf':csrf_token
          }
    html=session.post(GET_EXAM_SCHEDULE_URL,data=data,headers=USER_AGENT).text
    soup = BeautifulSoup(html, "html.parser")
    values = soup.find_all('td')[15:]

    result = {}
    subject_data = {}
    index = 1

    header = ['S.No.', 'Course Code', 'Course Title', 'Course Type', 'Class ID', 'Slot', 'Exam Date', 
            'Exam Session', 'Reporting Time', 'Exam Time', 'Venue', 'Seat Location', 'Seat No.']

    for i, value in enumerate(values, start=1):
        if i % 13 == 1:
            if subject_data:
                  result[index] = subject_data
                  subject_data = {}
                  index += 1
        key = header[i % 13 - 1]
        subject_data[key] = value.get_text().strip()

      # Adding the last subject data
    if subject_data:
      result[index] = subject_data

      #Write the data into a JSON file
    with open('exam_scledule.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)
