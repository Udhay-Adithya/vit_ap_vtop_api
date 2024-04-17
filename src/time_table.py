from .constants import TIME_TABLE_URL,GET_TIME_TABLE_URL, HEADERS
import time
from datetime import datetime,timezone
from .tools import parse_time_table

def get_time_table(session,username,csrf_token):
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
    print(html.content)
    return parse_time_table(html.text)