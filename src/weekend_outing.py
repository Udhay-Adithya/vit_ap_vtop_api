from requests import Session
from .constants import HEADERS, WEEKEND_OUTING_URL, SAVE_WEEKEND_OUTING_URL, EDIT_WEEKEND_OUTING_FORM, DELETE_WEEKEND_OUTING_FORM
import time
from datetime import datetime, timezone
from .parsers import outing_form_parser
from .utils import outing_response_checker

def post_weekend_outing_form(session: Session, username: str, csrf_token: str, outPlace: str, purposeOfVisit: str, outingDate: str, outTime: str, contactNumber: str) -> str:
    """
    Submits a weekend outing request form for a student.

    This function first initializes a request to fetch the necessary form information. It then
    sends the outing details to the server to save the form data. The response is processed to
    determine the outcome of the request.

    Args:
        session (Session): The session object used for making HTTP requests.
        username (str): The username of the student submitting the outing request.
        csrf_token (str): The CSRF token used for form validation.
        outPlace (str): The place where the student plans to visit.
        purposeOfVisit (str): The reason for the outing.
        outingDate (str): The date of the outing in the format "DD-MMM-YYYY".
        outTime (str): The time of departure in the format "HH:MM".
        contactNumber (str): The contact number of the student.

    Returns:
        str: A message indicating the result of the outing request submission.
    """
    # Prepare the initial request data to fetch form information
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    # Send the initial POST request to fetch the outing form
    initial_response = session.post(WEEKEND_OUTING_URL, data=data, headers=HEADERS)
    form_info = outing_form_parser.parse_outing_form(initial_response.text)
    
    # Prepare the data for submitting the outing request
    data = {
        'authorizedID': form_info["register_number"],
        'BookingId': '',
        'regNo': form_info["register_number"],
        'name': form_info["name"],
        'applicationNo': form_info["application_no"],
        'gender': form_info["gender"],
        'hostelBlock': form_info["hostel_block"],
        'roomNo': form_info["room_number"],
        'outPlace': outPlace,
        'purposeOfVisit': purposeOfVisit,
        'outingDate': outingDate,
        'outTime': outTime,
        'contactNumber': contactNumber,
        'parentContactNumber': form_info["parent_contact_number"],
        '_csrf': csrf_token,
        'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
    # Send the POST request to save the weekend outing form
    response = session.post(SAVE_WEEKEND_OUTING_URL, data=data, headers=HEADERS)
    
    # Process and return the response message
    return outing_response_checker.find_outing_response(response.text)
