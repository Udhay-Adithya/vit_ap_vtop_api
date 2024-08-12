from bs4 import BeautifulSoup


def login_error_identifier(html : str) -> str:
    """
    Extracts the login error message from HTML content.

    Args:
        html (str): The HTML content containing the login page.

    Returns:
        str or Error message: The extracted login error message if found, 
        or an error occurs during parsing.
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        err_msg = soup.find('strong')
        
        if err_msg:
            # Return the text content of the error message
            return err_msg.get_text(strip=True)
        else:
            return "Unable to find login response"
    
    except Exception as e:
        # Handle any exceptions that may occur during parsing
        return f"Unknown error occured during login : {e}"