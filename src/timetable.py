from .constants import TIME_TABLE_URL,GET_TIME_TABLE_URL, HEADERS
import time
from datetime import datetime,timezone
from .parsers import timetable_parser

def get_timetable(session,username,semSubID,csrf_token)-> (dict[str, dict] | None):
      data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
      initial_response = session.post(TIME_TABLE_URL,data=data,headers=HEADERS)
      data={'_csrf':csrf_token,
          'semesterSubId':semSubID,
          'authorizedID':username,
          'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}
      html = session.post(GET_TIME_TABLE_URL,data=data,headers=HEADERS)
      return timetable_parser.parse_time_table(html.content)