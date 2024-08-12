import re


def find_csrf(html : str) -> str:
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
        return 'Unable to find CSRF token'