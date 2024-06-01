import re
from bs4 import BeautifulSoup



def login_error_identifier(html):
    """
    Extracts the login error message from HTML content.

    Args:
        html (str): The HTML content containing the login page.

    Returns:
        str or None: The extracted login error message if found, 
        or None if no error message is found or an error occurs during parsing.
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        err_msg = soup.find('strong')
        
        if err_msg:
            # Return the text content of the error message
            return err_msg.get_text(strip=True)
        else:
            return None
    
    except Exception as e:
        # Handle any exceptions that may occur during parsing
        print(f"Error occurred: {e}")
        return None



def find_csrf(html):
    """
    Finds and returns the CSRF token from HTML content.

    Args:
        html (str): The HTML content to search for the CSRF token.

    Returns:
        str: The CSRF token if found, otherwise None.
    """    
    #Search for the csrfValue using the regular expression
    pattern = r'<input type="hidden" name="_csrf" value="([0-9a-f-]+)"'
    match=re.search(pattern, html)
    if match:
        return match.group(1)
    else:
        return 'Null'



def find_captcha(html):
    """
    Finds and returns the base64 code of the captcha from HTML content.

    Args:
        html (str): The HTML content to search for the captcha.

    Returns:
        str: The base64 code of the captcha if found, otherwise 'Null'.
    """
    pattern = r'data:image/jpeg;base64,([^"]+)'
    match=re.search(pattern, html)
    if match:
        return match.group(1)
    else:
        return 'Null'

def extract_pfp_base64(html):
    """
    Finds and returns the base64 code of the users profile photo from HTML content.

    Args:
        html (str): The HTML content to search for the captcha.

    Returns:
        str: The base64 code of the users profile photo if found, otherwise 'Unable to find User Profile'.
    """
    soup = BeautifulSoup(html, "html.parser")
    userProfileTag = soup.find("img", class_="img border border-primary")
    
    if userProfileTag:
        src_value = userProfileTag.get("src")
        if src_value and src_value.startswith("data:"):
            base64_code = src_value.split(",")[1]
            return base64_code
    return "Unable to find User Profile"