# This method call both pending and completed payment
from .pending_payments import get_pending_payments
from .payment_receipts import get_payment_receipts

def get_payments(session, username, applno,csrf_token):
    return {'payment_dues' : get_pending_payments(session, username, csrf_token),
            'payment_receipts' : get_payment_receipts(session, username, applno,csrf_token)}