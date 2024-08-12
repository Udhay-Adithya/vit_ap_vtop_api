import requests
from .constants import PROFILE_URL, HEADERS
from .utils import extract_stu_pfp
from .mentor_details import mentor_details
from .hod_details import hod_details
from .grade_history import get_grade_history
import time
from bs4 import BeautifulSoup

def stu_profile(session : requests.Session, username : str, csrf_token : str) -> dict :
    """
    Retrieves and compiles the student profile information from the VTOP system.

    This function fetches the student's profile page, parses the HTML to extract 
    various details, and then compiles this information into a dictionary. It 
    also retrieves additional data such as profile picture, mentor details, 
    HOD details, and grade history.

    Parameters:
    -----------
    session : requests.Session
        The session object used for making HTTP requests.
    username : str
        The username of the student whose profile information is being retrieved.
    csrf_token : str
        The CSRF token required for authentication with the VTOP system.

    Returns:
    --------
    dict
        A dictionary containing:
        - 'pfp': The base64 encoded profile picture of the student.
        - 'mentor_details': Details of the student's mentor.
        - 'hod_and_dean_info': Details of the HOD and dean.
        - 'grade_history': The student's grade history.
        - 'application_number': The student's application number.
        - 'student_name': The student's name.
        - 'dob': The student's date of birth.
        - 'gender': The student's gender.
        - 'blood_group': The student's blood group.
        - 'email': The student's email address.
    """
    
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    
    html = session.post(PROFILE_URL, data=data, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")
    user_data = soup.find_all('td')

    profile_data = {
        "pfp": extract_stu_pfp.extract_pfp_base64(html),
        "mentor_details": mentor_details(session, username, csrf_token),
        "hod_and_dean_info": hod_details(session, username, csrf_token),
        "grade_history": get_grade_history(session, username, csrf_token)
    }
    
    for i in range(len(user_data)):
        text = user_data[i].get_text().strip()
        if text == "APPLICATION NUMBER":
            profile_data["application_number"] = user_data[i+1].get_text().strip()
        elif text == "STUDENT NAME":
            profile_data["student_name"] = user_data[i+1].get_text().strip()
        elif text == "DATE OF BIRTH":
            profile_data["dob"] = user_data[i+1].get_text().strip()
        elif text == "GENDER":
            profile_data["gender"] = user_data[i+1].get_text().strip()
        elif text == "BLOOD GROUP":
            profile_data["blood_group"] = user_data[i+1].get_text().strip()
        elif text == "EMAIL":
            profile_data["email"] = user_data[i+1].get_text().strip()

    return profile_data
