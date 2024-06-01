from bs4 import BeautifulSoup
from .constants import VIEW_ATTENDENCE_URL,ATTENDENCE_URL,HEADERS
import time
from datetime import datetime,timezone
from .parser import attendence_parser

def get_attendence(session,username,semSubID,csrf_token):
      try:
        data={'verifyMenu':'true',
            'authorizedID':username,
            '_csrf' : csrf_token,
            'nocache':int(round(time.time() * 1000))}
        initial_post=session.post(ATTENDENCE_URL,data=data,headers=HEADERS)
      except Exception as e :
          print(e)      
      try:
        data={'_csrf':csrf_token,
            'semesterSubId':semSubID,
            'authorizedID':username,
            'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}
        html=session.post(VIEW_ATTENDENCE_URL,data=data,headers=HEADERS)
      except Exception as e :
          print(e)
      soup = BeautifulSoup(html.content,"html.parser")
      base= soup.find_all('table',id='AttendanceDetailDataTable')
      if base:
        return attendence_parser(base)
      else:
         return f"Error : {base}"
