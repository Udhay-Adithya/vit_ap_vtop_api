from .constants import VIEW_ATTENDANCE_URL, ATTENDANCE_URL, HEADERS
import time
from datetime import datetime, timezone
from .parsers import attendance_parser

def get_attendance(
    session, username: str, semSubID: str, csrf_token: str
) -> dict:
    """
    Retrieves the attendance details for a specific user and semester subject.

    This function performs two HTTP POST requests to the VTOP system. The first request is used to verify the user's session,
    and the second request fetches the attendance data for the given semester subject. The data is then parsed and returned 
    as a dictionary.

    Parameters:
        session (requests.Session): 
            The active session object used for maintaining the user's session.
        username (str): 
            The username of the student whose attendance data is being retrieved.
        semSubID (str): 
            The identifier for the semester subject.
        csrf_token (str): 
            The CSRF token required to authenticate the request.

    Returns:
        dict: 
            A dictionary containing the parsed attendance data. If the data cannot be retrieved, an error message is returned.
    """
    try:
        data = {
            "verifyMenu": "true",
            "authorizedID": username,
            "_csrf": csrf_token,
            "nocache": int(round(time.time() * 1000)),
        }
        initial_post = session.post(ATTENDANCE_URL, data=data, headers=HEADERS)
    except Exception as e:
        print(e)
    
    try:
        data = {
            "_csrf": csrf_token,
            "semesterSubId": semSubID,
            "authorizedID": username,
            "x": datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT"),
        }
        html = session.post(VIEW_ATTENDANCE_URL, data=data, headers=HEADERS)
    except Exception as e:
        print(e)

    if html:
        return attendance_parser.parse_attendance(html.text)
    else:
        return {"Error" : "Unable to find attendance details"}
