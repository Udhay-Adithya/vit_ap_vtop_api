from typing import List, Dict
from .constants import *
import time
from .parsers import exam_schedule_parser

def get_exam_schedule(session, username: str, semesterSubId: str, csrf_token) -> List[Dict]:
    """
    Retrieves the exam schedule for a specific user and semester.

    This function sends two HTTP POST requests to the VTOP system. The first request verifies the user's session,
    and the second request retrieves the exam schedule for the specified semester. The HTML content is parsed using
    a custom parser to extract and organize the exam schedule details into a list of dictionaries.

    Parameters:
        session (requests.Session): 
            The active session object used for maintaining the user's session.
        username (str): 
            The username of the student whose exam schedule is being retrieved.
        semesterSubId (str): 
            The semester identifier for which the exam schedule is requested.
        csrf_token (str): 
            The CSRF token required to authenticate the request.

    Returns:
        list[dict]:
            A list containing the parsed exam schedule details, including course codes, exam dates, and timings.
    """
    data = {
        "verifyMenu": "true",
        "authorizedID": username,
        "_csrf": csrf_token,
        "nocache": int(round(time.time() * 1000)),
    }
    session.post(EXAM_SCHEDULE_URL, data=data, headers=HEADERS)
    
    data = {
        "authorizedID": username,
        "semesterSubId": semesterSubId,
        "_csrf": csrf_token,
    }
    html = session.post(GET_EXAM_SCHEDULE_URL, data=data, headers=HEADERS)
    return exam_schedule_parser.parse_exam_schedule(html.content)
