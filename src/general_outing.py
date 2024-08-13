from requests import Session
from .constants import HEADERS, GENERAL_OUTING_URL, SAVE_GENERAL_OUTING_URL
from .parsers import outing_form_parser
from .utils import outing_response_checker
import time
from datetime import datetime, timezone

def post_general_outing_form(session: Session, username: str, csrf_token: str, outPlace: str, purposeOfVisit: str, outingDate: str, outTime: str,inDate: str, inTime: str,) -> str:
    """
    Submits a general outing form for a student in the VTOP system.

    This function handles the submission of a general outing form by first retrieving the student's form details
    and then posting the filled form data to the server. The form includes information such as the place of visit,
    purpose, outing date, and time, as well as contact details.

    Parameters:
        session (Session): 
            The active session object used to maintain the user's session.
        username (str): 
            The username of the student submitting the outing form.
        csrf_token (str): 
            The CSRF token required to authenticate the request.
        outPlace (str): 
            The place of visit for the outing.
        purposeOfVisit (str): 
            The purpose of the visit.
        outingDate (str): 
            The date of the outing in the format 'DD-MMM-YYYY'.
        outTime (str): 
            The time of departure in the format 'HH:MM'.
        inDate (str): 
            The date of return from outing in the format 'DD-MMM-YYYY'.
        inTime (str): 
            The expected time of return in the format 'HH:MM'.
        contactNumber (str): 
            The contact number of the student.

    Returns:
        str: 
            A string indicating the result of the outing form submission, such as success or failure messages.
    """
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    intial_response = session.post(GENERAL_OUTING_URL, data=data, headers=HEADERS)
    form_info = outing_form_parser.parse_outing_form(intial_response.text)

    data = {
        'authorizedID': form_info["register_number"],
        'LeaveId' : '',
        'regNo' : form_info["register_number"],
        'name' : form_info["name"],
        'applicationNo' : form_info["application_no"],
        'gender' : form_info["gender"],
        'hostelBlock' : form_info["hostel_block"],
        'roomNo' : form_info["room_number"],
        'placeOfVisit' : outPlace,
        'purposeOfVisit' : purposeOfVisit,
        'outDate' : outingDate,
        'outTimeHr' : outTime.split(":")[0],
        'outTimeMin' : outTime.split(":")[1],
        'inDate' : inDate,
        'inTimeHr' : inTime.split(":")[0],
        'inTimeMin' : inTime.split(":")[1],
        'parentContactNumber' : form_info["parent_contact_number"],
        '_csrf' : csrf_token,
        'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
    
    response = session.post(SAVE_GENERAL_OUTING_URL, data=data, headers=HEADERS)
    return outing_response_checker.find_outing_response(response.text)
