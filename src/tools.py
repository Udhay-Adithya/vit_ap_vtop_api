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