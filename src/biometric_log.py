from .constants import *
from .tools import find_csrf
import time
import json
from bs4 import BeautifulSoup
from datetime import datetime,timezone

def get_biometric(session,username,csrf_token):
    data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
    session.post(BIOMETRIC_LOG_URL,data=data,headers=HEADERS)
    data={'_csrf':csrf_token,
          'fromDate':'13/03/2024',
          'authorizedID':username,
          'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}
    html=session.post(GET_BIOMETRIC_LOG_URL,data=data,headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")
    user_data = soup.find_all('td')
    # Create a list to store the extracted data
    extracted_data = []

    # Iterate over the user_data starting from the second row (skipping headers)
    for i in range(4, len(user_data), 4):  # Start from index 4
        biometric_entry = {
            'entry_number': user_data[i].get_text(),
            'date': user_data[i+1].get_text(),
            'location': user_data[i+3].get_text().strip()
        }
        extracted_data.append(biometric_entry)

    # Convert extracted_data to JSON format
    json_data = json.dumps(extracted_data)

    print(json_data)