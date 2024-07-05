from .constants import *
import time
from .parsers import exam_schedule_parser

def get_exam_schedule(session,username,semesterSubId,csrf_token):
    data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
    session.post(EXAM_SCHEDULE_URL,data=data,headers=HEADERS)
    data={'authorizedID':username,
          'semesterSubId':semesterSubId,
          '_csrf':csrf_token
          }
    html=session.post(GET_EXAM_SCHEDULE_URL,data=data,headers=HEADERS)
    if html:
        return exam_schedule_parser.parse_exam_schedule(html.content)
    else :
        return "Unable to find exam schedule"