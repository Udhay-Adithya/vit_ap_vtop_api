import re


def find_hod_image(html : str) -> str:
    """
    Finds and returns the base64 code of the HOD or Dean's profile photo from HTML content.

    Args:
        html (str): The HTML content to search for the captcha.

    Returns:
        str: The base64 code of the HOD or Dean's profile photo if found, otherwise 'Unable to find HOD's profile photo'.
    """
    pattern = r'data:JPEG;base64,([^"]+)'
    match=re.search(pattern, html)
    if match:
        return match.group(1)
    else:
        return 'Unable to find HOD\'s profile photo'