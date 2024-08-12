from bs4 import BeautifulSoup


def extract_pfp_base64(html : str) -> str:
    """
    Finds and returns the base64 code of the users profile photo from HTML content.

    Args:
        html (str): The HTML content to search for the captcha.

    Returns:
        str: The base64 code of the users profile photo if found, otherwise 'Unable to find User profile photo'.
    """
    soup = BeautifulSoup(html, "html.parser")
    userProfileTag = soup.find("img", class_="img border border-primary")
    
    if userProfileTag:
        src_value = userProfileTag.get("src")
        if src_value and src_value.startswith("data:"):
            base64_code = src_value.split(",")[1]
            return base64_code
    return "Unable to find User profile photo"