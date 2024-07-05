from .constants import HEADERS,PAYMENT_RECEIPT_URL
import time
from .parsers import payments_receipts_parser

def get_payment_receipts(session, username, csrf_token):
    data = {'verifyMenu': 'true',
            'authorizedID': username,
            '_csrf': csrf_token,
            'nocache': int(round(time.time() * 1000))}
    
    html = session.post(PAYMENT_RECEIPT_URL, data=data, headers=HEADERS)
    if html:
        return payments_receipts_parser.parse_payment_receipts(html.text)
    else:
        return "Unable to find payment receipts info"