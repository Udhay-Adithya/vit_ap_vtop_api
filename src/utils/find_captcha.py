import re


def find_captcha(html):
    """
    Finds and returns the base64 code of the captcha from HTML content.

    Args:
        html (str): The HTML content to search for the captcha.

    Returns:
        str: The base64 code of the captcha if found, otherwise 'Null'.
    """
    pattern = r'data:image/jpeg;base64,([^"]+)'
    match = re.search(pattern, html)
    if match:
        return match.group(1)
    else:
        return 'Null'