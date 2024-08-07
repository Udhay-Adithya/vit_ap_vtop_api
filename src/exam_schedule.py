from .constants import *
import time
from .parsers import exam_schedule_parser


def get_exam_schedule(session, username: str, semesterSubId: str, csrf_token) -> dict:
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
