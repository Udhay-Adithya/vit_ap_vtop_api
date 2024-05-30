from .constants import HEADERS,BIOMETRIC_LOG_URL,GET_BIOMETRIC_LOG_URL
import time
from bs4 import BeautifulSoup
from datetime import datetime,timezone

def get_biometric(session, username, date, csrf_token):
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
