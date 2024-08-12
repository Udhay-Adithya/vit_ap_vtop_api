import time
from bs4 import BeautifulSoup
from .constants import HEADERS, NCGPA_RANK_URL

def ncgpa_rank_details(session, username, csrf_token):
    """
    Retrieves the NCGPA rank details for a specified user from the VTOP system.

    Sends a POST request to the NCGPA Rank URL with the provided authentication and 
    CSRF token to obtain the NCGPA rank information for the user.

    Parameters:
    -----------
    session : requests.Session
        The session object used for making HTTP requests.
    username : str
        The username of the user whose NCGPA rank details are being requested.
    csrf_token : str
        The CSRF token required for authentication with the VTOP system.

    Returns:
    --------
    dict
        A dictionary containing the NCGPA rank details if the request is successful.
        The dictionary includes the rank, OTP, and group. If the details cannot be 
        retrieved or if there is an error during parsing, the dictionary will contain 
        an error message for the rank.
    """
    
    ncgpa_rank = {}
    data = {
        'verifyMenu': 'true',
        'authorizedID': username,
        '_csrf': csrf_token,
        'nocache': int(round(time.time() * 1000))
    }

    html = session.post(NCGPA_RANK_URL, data=data, headers=HEADERS)
    if html:
        try:
            soup = BeautifulSoup(html.content, 'html.parser')
            htmltable = soup.find_all('tr')
            ncgpa_rank["rank"] = htmltable[0].get_text().split()[5]
            ncgpa_rank["otp"] = htmltable[1].get_text().split()[1]
            ncgpa_rank["group"] = htmltable[2].get_text().split()[4]
            return ncgpa_rank
        except:
            ncgpa_rank["rank"] = "Unable to find NCGPA rank details"
            return ncgpa_rank
    else:
        ncgpa_rank["rank"] = "Unable to find NCGPA rank details"
        return ncgpa_rank
