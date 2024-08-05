from .constants import HEADERS,GRADE_HISTORY_URL
import time
from .parsers import grades_details_parser

def get_grade_history(session, username, csrf_token):
    data = {'verifyMenu': 'true',
            'authorizedID': username,
            '_csrf': csrf_token,
            'nocache': int(round(time.time() * 1000))}
    
    html = session.post(GRADE_HISTORY_URL, data=data, headers=HEADERS)
    if html:
        return grades_details_parser.parse_grade_history(html.text)
    else:
        return "Unable to find grade history"