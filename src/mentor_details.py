from .constants import *
import time
from .parsers import mentor_parser

def mentor_details(session, username, csrf_token):
    data = {'verifyMenu': 'true',
            'authorizedID': username,
            '_csrf': csrf_token,
            'nocache': int(round(time.time() * 1000))}
    
    html = session.post(MENTOR_DETAILS_URL, data=data, headers=HEADERS)
    if html:
        return mentor_parser.mentor_details_parser(html.content)
    else:
        return "Unable to find mentor info"