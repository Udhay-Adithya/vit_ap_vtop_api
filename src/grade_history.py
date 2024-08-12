from requests import Session
from .constants import HEADERS, GRADE_HISTORY_URL
import time
from .parsers import grades_details_parser

def get_grade_history(session: Session, username: str, csrf_token: str) -> dict:
    """
    Fetches the grade history of a student from the VTOP system.

    This function sends a POST request to retrieve the student's grade history and parses the response 
    using the `grades_details_parser`. If the request is successful, it returns the parsed grade history 
    as a dictionary. Otherwise, it returns an error message.

    Parameters:
        session (Session): 
            The active session object used to maintain the user's session.
        username (str): 
            The username of the student whose grade history is being retrieved.
        csrf_token (str): 
            The CSRF token required to authenticate the request.

    Returns:
        dict or str: 
            A dictionary containing the parsed grade history if successful, otherwise an error message.
    """
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }

    html = session.post(GRADE_HISTORY_URL, data=data, headers=HEADERS)
    
    if html:
        return grades_details_parser.parse_grade_history(html.text)
    else:
        return "Unable to find grade history"
