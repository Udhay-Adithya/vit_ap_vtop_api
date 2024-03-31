from .constants import *
from .tools import find_csrf
import time
import json
from bs4 import BeautifulSoup

def mentor_details(session, username, csrf_token):
    data = {'verifyMenu': 'true',
            'authorizedID': username,
            '_csrf': csrf_token,
            'nocache': int(round(time.time() * 1000))}
    
    html = session.post(MENTOR_DETAILS_URL, data=data, headers=USER_AGENT).text

    soup = BeautifulSoup(html, "html.parser")
    mentor_data = soup.find_all('td')
    mentor_details_dict = {}


    # Handling 'Faculty ID' separately
    faculty_id = soup.find('td', string=' Faculty ID')
    if faculty_id:
        mentor_details_dict[faculty_id.get_text().strip()] = faculty_id.find_next('td').get_text().strip()

    # Handling other rows
    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 2:
            key = columns[0].get_text().strip()
            value = columns[1].get_text().strip()
            mentor_details_dict[key] = value

    with open('mentor_details.json', 'w') as json_file:
        json.dump(mentor_details_dict, json_file, indent=4)