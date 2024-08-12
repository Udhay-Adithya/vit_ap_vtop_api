from .constants import TIME_TABLE_URL, GET_TIME_TABLE_URL, HEADERS
import time
from datetime import datetime, timezone
from .parsers import timetable_parser

def get_timetable(session, username, semSubID, csrf_token) -> dict[str, list]:
    """
    Retrieves the timetable for a specified semester and user.

    This function sends two POST requests: the first to initialize the request and the second
    to fetch the actual timetable data. The response is then parsed to extract the timetable information.

    Args:
        session (requests.Session): The session object used for making HTTP requests.
        username (str): The username of the student or user.
        semSubID (str): The semester subject ID for which the timetable is to be fetched.
        csrf_token (str): The CSRF token used for form validation.

    Returns:
        dict[str, dict] | None: A dictionary containing the timetable details parsed from the response.
        Returns None if the timetable could not be fetched or parsed.
    """
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    initial_response = session.post(TIME_TABLE_URL, data=data, headers=HEADERS)
    data = {
        '_csrf': csrf_token,
        'semesterSubId': semSubID,
        'authorizedID': username,
        'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
    html = session.post(GET_TIME_TABLE_URL, data=data, headers=HEADERS)
    return timetable_parser.parse_time_table(html.content)
