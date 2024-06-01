from .constants import TIME_TABLE_URL,GET_TIME_TABLE_URL, HEADERS
import time
from datetime import datetime,timezone
from .parser import parse_time_table

def get_time_table(session,username,semSubID,csrf_token):
      data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
      initial_post=session.post(TIME_TABLE_URL,data=data,headers=HEADERS)
      data={'_csrf':csrf_token,
          'semesterSubId':semSubID,
          'authorizedID':username,
          'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}
      html=session.post(GET_TIME_TABLE_URL,data=data,headers=HEADERS)
      return parse_time_table(html.content)