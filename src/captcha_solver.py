import base64
import os 
import io
import json 
import numpy as np 
from PIL import Image
import requests
from .constants import VTOP_LOGIN_URL, HEADERS
from .tools import find_captcha

MAX_RETRIES=5
def fetch_and_display_captcha(session, retries=MAX_RETRIES):
    """
    Fetches CSRF token from the VTOP website and performs pre-login request.

    Args:
        session (requests.Session): Session object for making HTTP requests.
        retries (int): Number of retries for fetching captcha.

    Returns:
        str or False: Base64 encoded captcha image or False if not found.
    """
    try:
        html = session.get(VTOP_LOGIN_URL, headers=HEADERS).text
        base64_code = find_captcha(html)
        if base64_code != 'Null':
            return base64_code
        elif retries > 0:
            print(f"Retrying... {retries} retries left.")
            return fetch_and_display_captcha(session, retries - 1)
        else:
            print("Maximum retries reached. Captcha not found.")
            return None
    except requests.RequestException as e:
        print("Failed to fetch captcha:", e)
        return False


curr_dir = os.path.dirname(__file__)
print(curr_dir)
# Loading the ML Model 
WEIGHTS_FILE_PATH = os.path.join(curr_dir, "weights.json")
print(WEIGHTS_FILE_PATH)
with open(WEIGHTS_FILE_PATH, "r") as f:
    model_config = json.load(f)

weights = np.array(model_config["weights"])
biases = np.array(model_config["biases"])

def partition_img(img: np.ndarray) -> list[np.ndarray]:
    parts = [] 
    for i in range(6):
        x1 = (i + 1) * 25 + 2
        y1 = 7 + 5 * (i % 2) + 1
        x2 = (i + 2) * 25 + 1
        y2 = 35 - 5 * ((i + 1) % 2)
        # select the bounding box 
        part = img[y1:y2, x1:x2]
        parts.append(part)
    return parts

def convert_to_abs_bw(img: np.ndarray) -> np.ndarray:
    avg = np.sum(img)
    avg /= 24 * 22
    return np.where(img > avg, 0, 1)

def solve_captcha(captcha: str) -> str: 
    img = _str_to_img(captcha)
    # img = convert_to_abs_bw(img)
    img = partition_img(img)
    return _solve_captcha_ml(img)

def _solve_captcha_ml(img: list[np.ndarray]) -> str:
    LETTERS = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    captcha = ""
    for single_letter in img:
        dw_img = convert_to_abs_bw(single_letter)
        dw_img = dw_img.flatten()
        x = np.dot(dw_img, weights) + biases
        x = np.exp(x)
        captcha += LETTERS[np.argmax(x)]
    return captcha

def _str_to_img(src: str) -> np.ndarray:
    # decoding the base64 string i.e string -> bytes -> image
    im = base64.b64decode(src)
    img = Image.open(io.BytesIO(im)).convert("L")
    # img.save("./_test/saves/img.png")
    img = np.array(img)
    return img