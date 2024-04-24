from .constants import VTOP_CONTENT_URL,TIME_TABLE_URL,GET_TIME_TABLE_URL, HEADERS
import time
from datetime import datetime,timezone
from .tools import find_csrf
from .parser import parse_time_table

def get_time_table(session,username):
      response = session.get(VTOP_CONTENT_URL, headers=HEADERS).text
      csrf_token = find_csrf(response)
      data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
      response=session.post(TIME_TABLE_URL,data=data,headers=HEADERS)
      data={'_csrf':csrf_token,
          'semesterSubId':'AP2023247',
          'authorizedID':username,
          'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}
      html=session.post(GET_TIME_TABLE_URL,data=data,headers=HEADERS)
      return parse_time_table(html.content)