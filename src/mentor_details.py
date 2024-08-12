import requests
from .constants import HEADERS,MENTOR_DETAILS_URL
import time
from .parsers import mentor_parser

def mentor_details(session:requests.Session, username:str, csrf_token:str) -> dict:
    """
    Retrieves the mentor details for a specified user from the VTOP system.

    Sends a POST request to the Mentor Details URL with the provided authentication and 
    CSRF token to obtain the mentor information for the user.

    Parameters:
    -----------
    session : requests.Session
        The session object used for making HTTP requests.
    username : str
        The username of the user whose mentor details are being requested.
    csrf_token : str
        The CSRF token required for authentication with the VTOP system.

    Returns:
    --------
    dict
        A dictionary containing the parsed mentor details if the request is successful.
        The dictionary is obtained by parsing the HTML response using the 
        `mentor_parser.mentor_details_parser` function or
        An error message if the mentor details could not be retrieved.
    """

    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    html = session.post(MENTOR_DETAILS_URL, data=data, headers=HEADERS)
    if html:
        return mentor_parser.mentor_details_parser(html.content)
    else:
        return {"error" : "Unable to find mentor info"}
