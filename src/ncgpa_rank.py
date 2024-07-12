import time
from bs4 import BeautifulSoup
from .constants import HEADERS,NCGPA_RANK_URL
import time

def ncgpa_rank_details(session, username, csrf_token):
    ncgpa_rank={}
    data = {'verifyMenu': 'true',
            'authorizedID': username,
            '_csrf': csrf_token,
            'nocache': int(round(time.time() * 1000))}
    
    html = session.post(NCGPA_RANK_URL, data=data, headers=HEADERS)
    if html:
        try:
            soup = BeautifulSoup(html.content,'html.parser')
            htmltable = soup.find_all('tr')
            ncgpa_rank["rank"]=htmltable[0].get_text().split()[5]
            ncgpa_rank["otp"]=htmltable[1].get_text().split()[1]
            ncgpa_rank["group"]=htmltable[2].get_text().split()[4]
            return ncgpa_rank
        except:
            ncgpa_rank["rank"]="Unable to find NCGPA rank details"
            return ncgpa_rank
    else:
        ncgpa_rank["rank"]="Unable to find NCGPA rank details"
        return ncgpa_rank