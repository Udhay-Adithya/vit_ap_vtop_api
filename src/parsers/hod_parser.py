import re
from bs4 import BeautifulSoup

def hod_details_parser(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Initialize dictionary to store extracted data
    hod_dict = {}

    # Extract title from box-header with-border text-center
    title_element = soup.find('div', class_='box-header with-border text-center')
    if title_element:
        title = title_element.text.strip()
        hod_dict['title'] = title

    # Extract table data
    table = soup.find('table', class_='table')
    if table:
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) == 2:
                key = columns[0].text.strip()
                value = columns[1].text.strip()
                hod_dict[key] = value
                pattern = r'data:JPEG;base64,([^"]+)'
                match=re.search(pattern, html)
                if match:
                    hod_dict['image_base64'] = match.group(1)
                else:
                    hod_dict['image_base64'] = "No image found"
    return hod_dict