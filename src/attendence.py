from bs4 import BeautifulSoup
from .constants import VTOP_CONTENT_URL,ATTENDENCE_URL,GET_ATTENDENCE_URL, HEADERS
import time
from datetime import datetime,timezone
from .parser import attendence_parser
from .tools import find_csrf

def get_time_table(session,username):
      try:
        response = session.get(VTOP_CONTENT_URL, headers=HEADERS).text
        csrf_token = find_csrf(response)
        data={'_csrf':csrf_token,
            'semesterSubId':'AP2023247',
            'authorizedID':username,
            'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}
        html=session.post(ATTENDENCE_URL,data=data,headers=HEADERS)
      except Exception as e :
          print(e)
      soup = BeautifulSoup(html,"html.parser")
      base= soup.find_all('table',id='AttendanceDetailDataTable')
      return attendence_parser(base)
