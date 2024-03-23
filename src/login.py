from constants import *
import base64
import PIL.Image as Image
from tools import *
import io


def prelogin(session):
    html=session.get(VTOP_URL,headers=USER_AGENT).text
    csrf_token = find_csrf(html)
    data={'_csrf':csrf_token,
          'flag':'VTOP'}
    session.post(VTOP_PRELOGIN_URL,data=data)

def captcha(session):
    html=session.get(VTOP_LOGIN_URL,headers=USER_AGENT).text
    base64_code = find_captcha(html)
    if base64_code:
        captcha_img_binary = base64.b64decode(base64_code)
        img = Image.open(io.BytesIO(captcha_img_binary))
        img.show()
    else:
        return None

def login(username,password,session,captcha_value):
    html=session.get(VTOP_LOGIN_URL,headers=USER_AGENT).text
    csrf_token=find_csrf(html)
    print(csrf_token)
    data={'_csrf':csrf_token,
          'username':username,
          'password':password,
          'captchaStr':captcha_value}
    print(session.post(VTOP_LOGIN_URL,data=data,headers=USER_AGENT))
    print(session.get(VTOP_CONTENT_URL,headers=USER_AGENT).text)
