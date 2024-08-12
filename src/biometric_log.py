from .constants import HEADERS, BIOMETRIC_LOG_URL, GET_BIOMETRIC_LOG_URL
import time
from bs4 import BeautifulSoup
from datetime import datetime, timezone

def get_biometric(session, username, date, csrf_token):
    """
    Retrieves biometric log details for a specific user and date.

    This function sends two HTTP POST requests to the VTOP system. The first request verifies the user's session,
    and the second request retrieves the biometric log data for the given date. The HTML content is parsed using 
    BeautifulSoup, and the biometric data is extracted and organized into a dictionary.

    Parameters:
        session (requests.Session): 
            The active session object used for maintaining the user's session.
        username (str): 
            The username of the student whose biometric data is being retrieved.
        date (str): 
            The date for which the biometric log is requested, in 'dd-mm-yyyy' format.
        csrf_token (str): 
            The CSRF token required to authenticate the request.

    Returns:
        dict: 
            A dictionary containing the biometric logs, with each entry's time and location. 
            The key is the specific entry date and time.
    """
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }
    session.post(BIOMETRIC_LOG_URL, data=data, headers=HEADERS)
    
    data = {
        '_csrf': csrf_token,
        'fromDate': date,
        'authorizedID': username,
        'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
    }
    html = session.post(GET_BIOMETRIC_LOG_URL, data=data, headers=HEADERS)
    soup = BeautifulSoup(html.content, "html.parser")
    bio_data = soup.find_all('td')
    
    biometric_logs = {}
    
    # Iterate over the bio_data starting from the second row (skipping headers)
    for i in range(4, len(bio_data), 4):  # Start from index 4
        biometric_log = {
            'time': bio_data[i+2].get_text(),
            'location': bio_data[i+3].get_text().strip().replace(' ', '')
        }
        biometric_logs[bio_data[i].get_text()] = biometric_log
    
    return biometric_logs
