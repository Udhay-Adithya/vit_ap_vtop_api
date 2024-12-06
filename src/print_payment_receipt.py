from datetime import datetime

import requests
from .constants import HEADERS, PRINT_PAYMENT_RECEIPT_URL
from .parsers import print_payment_parser


def print_payment_receipts(
    session: requests.Session, username: str, applno: str, csrf_token: str, receitNo: str,
) -> list:
    """
    Retrieves and processes payment receipts for a specified user from the VTOP system.

    Sends a POST request to obtain payment receipts and subsequently fetches detailed
    print pages for each receipt.

    Parameters:
    -----------
    session : requests.Session
        The session object used for making HTTP requests.
    username : str
        The username of the user whose payment receipts are being retrieved.
    applno : str
        The application number associated with the user for identifying specific receipts.
    csrf_token : str
        The CSRF token required for authentication with the VTOP system.

    Returns:
    --------
    dict
        A dictionary containing the payment receipts and their details. Each receipt
        is keyed by its receipt number and includes information like the receipt's details.
        If receipts cannot be retrieved, an error message is returned. If no receipts are
        found, a corresponding message is returned.
    """

    data = {
        "_csrf": csrf_token,
        "receitNo": receitNo,
        "applno": applno,
        "registerNumber": username,
        "x": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT"),
        "authorizedID": username,
    }

    html = session.post(PRINT_PAYMENT_RECEIPT_URL, data=data, headers=HEADERS)
    if html:
        return print_payment_parser.parse_print_payment_receipt_page(html.text)
    else:
        return {"error": "Unable to find payment receipts info"}
