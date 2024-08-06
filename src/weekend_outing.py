from requests import Session
from .constants import HEADERS,WEEKEND_OUTING_URL,SAVE_WEEKEND_OUTING_URL,EDIT_WEEKEND_OUTING_FORM,DELETE_WEEKEND_OUTING_FORM
import time
from datetime import datetime,timezone
from .parsers import weekend_outing_form_parser
from .utils import find_weekend_form_response

def post_weekend_outing_form(session : Session, username : str,csrf_token: str,outPlace: str,purposeOfVisit: str,outingDate: str,outTime: str,contactNumber: str) ->str:
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    intial_response = session.post(WEEKEND_OUTING_URL, data=data, headers=HEADERS)
    form_info = weekend_outing_form_parser.parse_outing_form(intial_response.text)
    data = {
        'authorizedID': form_info["register_number"],
        'BookingId' : '',
        'regNo' : form_info["register_number"],
        'name' : form_info["name"],
        'applicationNo' : form_info["application_no"],
        'gender' : form_info["gender"],
        'hostelBlock' : form_info["hostel_block"],
        'roomNo' : form_info["room_number"],
        'outPlace' : outPlace,
        'purposeOfVisit' : purposeOfVisit,
        'outingDate' : outingDate,
        'outTime' : outTime,
        'contactNumber' : contactNumber,
        'parentContactNumber' : form_info["parent_contact_number"],
        '_csrf' : csrf_token,
        'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
    response = session.post(SAVE_WEEKEND_OUTING_URL, data=data, headers=HEADERS)
    return find_weekend_form_response.find_weekend_message(response.text)
    
