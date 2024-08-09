from requests import Session
from .constants import HEADERS,GENERAL_OUTING_URL,SAVE_GENERAL_OUTING_URL,EDIT_GENRAL_OUTING_URL,DELETE_GENERAL_OUTING_URL
import time
from datetime import datetime,timezone
from .parsers import outing_form_parser
from .utils import outing_response_checker

def post_general_outing_form(session : Session, username : str,csrf_token: str,outPlace: str,purposeOfVisit: str,outingDate: str,outTime: str,inTime: str,contactNumber: str) -> str:
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    intial_response = session.post(GENERAL_OUTING_URL, data=data, headers=HEADERS)
    form_info = outing_form_parser.parse_outing_form(intial_response.text)
    # Note : outTime and inTime should be in the format of "HH : MM"
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
        'outTimeHr' : outTime.split(":")[0],
        'outTimeMin' : outTime.split(":")[1],
        'inTimeHr' : inTime.split(":")[0],
        'inTimeMin' : inTime.split(":")[1],
        'contactNumber' : contactNumber,
        'parentContactNumber' : form_info["parent_contact_number"],
        '_csrf' : csrf_token,
        'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
    response = session.post(SAVE_GENERAL_OUTING_URL, data=data, headers=HEADERS)
    return outing_response_checker.find_outing_response(response.text)
    
