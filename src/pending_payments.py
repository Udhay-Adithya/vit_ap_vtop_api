from .constants import HEADERS,PAYMENTS_URL
import time
from .parsers import pending_payments_parser

def get_pending_payments(session, username, csrf_token):
    data = {'verifyMenu': 'true',
            'authorizedID': username,
            '_csrf': csrf_token,
            'nocache': int(round(time.time() * 1000))}
    
    html = session.post(PAYMENTS_URL, data=data, headers=HEADERS)
    if html:
        return pending_payments_parser.pending_payments_parser(html.content)
    else:
        return "Unable to find pending payments"