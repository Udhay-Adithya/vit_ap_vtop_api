from datetime import datetime, timezone
from .constants import MARKS_URL, VIEW_MARKS_URL, HEADERS
import time
from .parsers import marks_parser

def get_marks(session, username, semSubID, csrf_token) -> (list | dict[str, str]) :
    """
    Retrieves all the available marks for a specified semester.

    This function sends two POST requests: the first to initialize the request the marks page and the second
    to fetch the actual marks. The response is then parsed to extract the marks information.

    Args:
        session (requests.Session): The session object used for making HTTP requests.
        username (str): The username of the student or user.
        semSubID (str): The semester subject ID for which the timetable is to be fetched.
        csrf_token (str): The CSRF token used for form validation.

    Returns:
        dict[str, dict] | None: A dictionary containing the marks parsed from the response.
        Returns None if the marks could not be fetched or parsed.
    """
    data = {
        "verifyMenu": "true",
        "authorizedID": username,
        "_csrf": csrf_token,
        "nocache": int(round(time.time() * 1000)),
    }
    initial_response = session.post(MARKS_URL, data=data, headers=HEADERS)
    print(
        f"""
{username} {semSubID} {csrf_token}
"""
          )
    data = {
        "authorizedID": username,
        "semesterSubId": semSubID,
        "_csrf": csrf_token,
        'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
    html = session.post(VIEW_MARKS_URL, data=data, headers=HEADERS)
    return marks_parser.marks_parser(html.text)
