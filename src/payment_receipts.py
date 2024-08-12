from datetime import datetime

import requests
from .constants import HEADERS, PAYMENT_RECEIPT_URL, PRINT_PAYMENT_RECEIPT_URL
import time
from .parsers import payments_receipts_parser, print_payment_parser


def get_payment_receipts(
    session: requests.Session, username: str, applno: str, csrf_token: str
) -> dict:
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
        "verifyMenu": "true",
        "authorizedID": username,
        "_csrf": csrf_token,
        "nocache": int(round(time.time() * 1000)),
    }

    html = session.post(PAYMENT_RECEIPT_URL, data=data, headers=HEADERS)
    if html:
        receipts = payments_receipts_parser.parse_payment_receipts(html.text)
        if receipts:
            print(receipts)
            for i in range(1, len(receipts) + 1):
                print(f" {i} : {type(i)}")
                data = {
                    "_csrf": csrf_token,
                    "receitNo": receipts[i]["receitNo"],
                    "applno": applno,
                    "registerNumber": username,
                    "x": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT"),
                    "authorizedID": username,
                }

                print_page = session.post(
                    PRINT_PAYMENT_RECEIPT_URL, data=data, headers=HEADERS
                )
                if print_page:
                    receipts[i] = print_payment_parser.parse_print_payment_receipt_page(
                        print_page.text, receipts, i
                    )
                else:
                    receipts[i][
                        "details"
                    ] = "Unable to retrieve details for this receipt"
            return receipts
        else:
            return {"error": "No receipts found"}
    else:
        return {"error": "Unable to find payment receipts info"}
