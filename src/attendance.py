from .constants import VIEW_ATTENDANCE_URL, ATTENDANCE_URL, HEADERS
import time
from datetime import datetime, timezone
from .parsers import attendance_parser


def get_attendance(
    session, username: str, semSubID: str, csrf_token: str
) -> dict | str:
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
        return f"Error : Unable to find attendence details"
