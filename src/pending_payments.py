import requests
from .constants import HEADERS, PAYMENTS_URL
import time
from .parsers import pending_payments_parser


def get_pending_payments(session: requests.Session, username: str, csrf_token: str) -> dict:
    """
    Retrieves pending payments information for a specified user from the VTOP system.

    Sends a POST request to obtain the list of pending payments and processes the response
    to extract relevant payment details.

    Parameters:
    -----------
    session : requests.Session
        The session object used for making HTTP requests.
    username : str
        The username of the user whose pending payments are being retrieved.
    csrf_token : str
        The CSRF token required for authentication with the VTOP system.

    Returns:
    --------
    dict
        A dictionary containing details of pending payments. If pending payments cannot
        be retrieved, an error message is returned.
    """

    data = {
        "verifyMenu": "true",
        "authorizedID": username,
        "_csrf": csrf_token,
        "nocache": int(round(time.time() * 1000)),
    }

    # Send a POST request to retrieve pending payments
    html = session.post(PAYMENTS_URL, data=data, headers=HEADERS)

    if html:
        # Parse and return pending payments from the response
        return pending_payments_parser.pending_payments_parser(html.content)
    else:
        return {"error": "Unable to find pending payments"}
