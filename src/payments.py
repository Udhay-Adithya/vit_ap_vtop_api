from .pending_payments import get_pending_payments
from .payment_receipts import get_payment_receipts

def get_payments(session, username, applno, csrf_token):
    """
    Retrieves both pending payment dues and payment receipts for a specified user.

    This function combines the results of two separate functions:
    - `get_pending_payments` to obtain the list of pending payments.
    - `get_payment_receipts` to obtain details of payment receipts.

    Parameters:
    -----------
    session : requests.Session
        The session object used for making HTTP requests.
    username : str
        The username of the user whose payment information is being retrieved.
    applno : str
        The application number of the user.
    csrf_token : str
        The CSRF token required for authentication with the VTOP system.

    Returns:
    --------
    dict
        A dictionary containing:
        - 'payment_dues': The result of the `get_pending_payments` function.
        - 'payment_receipts': The result of the `get_payment_receipts` function.
    """
    
    return {
        'payment_dues': get_pending_payments(session, username, csrf_token),
        'payment_receipts': get_payment_receipts(session, username, applno, csrf_token)
    }
