from constants import *
from tools import find_csrf
import time
import json
from bs4 import BeautifulSoup
from datetime import datetime,timezone

def get_time_table(session,username,csrf_token):
    data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
    html=session.post(TIME_TABLE_URL,data=data,headers=USER_AGENT)
    data={'_csrf':csrf_token,
          'semesterSubId':'AP2023247',
          'authorizedID':username,
          'x': datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")}
    html=session.post(GET_TIME_TABLE_URL,data=data,headers=USER_AGENT).text
    soup = BeautifulSoup(html, 'html.parser')

      # Find the table with id 'timeTableStyle'
    time_table = soup.find(id='timeTableStyle')
    list1, list2, list3, list4, list5 = [], [], [], [], []
    lst_table=[]
    if time_table:
    # Find all <tr> tags within the 'timeTableStyle' table starting from Tue
      tr_tags = time_table.find_all('tr')[4:]
    
    for tr_tag in tr_tags:
          tr_string = str(tr_tag.get_text(strip=False))
          # Split the string into lines
          lines=tr_string.split('\n')
          lines= list(filter(None, lines))
          lst_table.append(lines)
    else:
      print("No table with id 'timeTableStyle' found.")
      print(lst_table)