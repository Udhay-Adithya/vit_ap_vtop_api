from .constants import HEADERS, HOD_DETAILS_URL
import time
from .parsers import hod_parser

def hod_details(session, username, csrf_token):
    """
    Fetches the Head of Department (HOD) details for a given user from the VTOP system.

    Sends a POST request to the HOD details URL with the necessary authentication and CSRF 
    token to retrieve the HOD information for the user.
    
    Parameters:
    -----------
    session : requests.Session
        The session object used for making HTTP requests.
    username : str
        The username of the user whose HOD details are being requested.
    csrf_token : str
        The CSRF token required for authentication with the VTOP system.
    
    Returns:
    --------
    dict
        A dictionary containing the parsed HOD details if the request is successful.
        The dictionary is obtained by parsing the HTML response using the 
        `hod_parser.hod_details_parser` function.
    str
        An error message if the HOD details could not be retrieved.
    """

    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    html = session.post(HOD_DETAILS_URL, data=data, headers=HEADERS)
    if html:
        return hod_parser.hod_details_parser(html.text)
    else:
        return {"error" : "Unable to find HOD info"}
