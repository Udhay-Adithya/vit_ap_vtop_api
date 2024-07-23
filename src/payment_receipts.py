from datetime import datetime
from .constants import HEADERS,PAYMENT_RECEIPT_URL,PRINT_PAYMENT_RECEIPT_URL
import time
from .parsers import payments_receipts_parser,print_payment_parser

def get_payment_receipts(session, username, applno,csrf_token):
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    
    html = session.post(PAYMENT_RECEIPT_URL, data=data, headers=HEADERS)
    if html:
        receipts = payments_receipts_parser.parse_payment_receipts(html.text)
        if receipts:
            for i in range(1,(len(receipts)+1)):
                data = {
                    '_csrf': csrf_token,
                    'receitNo': receipts[i]['receitNo'],
                    'applno': applno,
                    'registerNumber': username,
                    'x': datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT'),
                    'authorizedID': username,
                }
        
                print_page = session.post(PRINT_PAYMENT_RECEIPT_URL, data=data, headers=HEADERS)
                if print_page:
                    receipts = print_payment_parser.parse_print_payment_receipt_page(print_page.text, receipts, i)
                else:
                    receipts[i]['details'] = "Unable to retrieve details for this receipt"
            return receipts
        else:
            return "No receipts found"
    else:
        return "Unable to find payment receipts info"