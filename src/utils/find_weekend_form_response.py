from bs4 import BeautifulSoup

def find_weekend_message(html_content : str) -> str:
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the <span> element with the specific class and style
    span = soup.find('span', class_='col-md-12', style='font-size: 20px; color: green; text-align: center;')
    
    # Return the text content of the span if found
    if span:
        return span.text.strip()
    else:
        return "Unable to find the response from VTOP. Please check VTOP manually for confirmation"