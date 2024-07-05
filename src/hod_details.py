from .constants import HEADERS,HOD_DETAILS_URL
import time
from .parsers import hod_parser

def hod_details(session, username, csrf_token):
    data = {'verifyMenu': 'true',
            'authorizedID': username,
            '_csrf': csrf_token,
            'nocache': int(round(time.time() * 1000))}
    
    html = session.post(HOD_DETAILS_URL, data=data, headers=HEADERS)
    if html:
        return hod_parser.hod_details_parser(html.text)
    else:
        return "Unable to find HOD info"