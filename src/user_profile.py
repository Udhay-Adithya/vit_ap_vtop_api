from constants import *
from tools import find_csrf
import time


def my_profile(session,username):
    csrf_token=find_csrf(session.get(VTOP_CONTENTS_URL).text)
    csrf_token=find_csrf(session.get(PROFILE_URL).text)
    print(csrf_token)
    data={'verifyMenu':'true',
          'authorizedID':username,
          '_csrf':csrf_token,
          'nocache':int(round(time.time() * 1000))}
    print(session.post(PROFILE_URL,data=data,headers=USER_AGENT))