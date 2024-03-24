from constants import *
from tools import find_csrf
import time
from bs4 import BeautifulSoup


def my_profile(session,username):
    csrf_token=find_csrf(session.get(VTOP_CONTENT_URL).text)
    data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
    html=(session.post(PROFILE_URL,data=data,headers=USER_AGENT).text)

    soup = BeautifulSoup(html, "html.parser")
    user_data = soup.find_all('td')
    f=open("stu_profile.text",'w')
    f.write(user_data)