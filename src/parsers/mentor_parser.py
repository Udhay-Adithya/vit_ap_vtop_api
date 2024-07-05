from bs4 import BeautifulSoup

def mentor_details_parser(html):
    soup = BeautifulSoup(html, "html.parser")
    mentor_details_dict = {}

    # Handling 'Faculty ID' separately
    faculty_id = soup.find('td', string=' Faculty ID')
    if faculty_id:
        mentor_details_dict[faculty_id.get_text().strip()] = faculty_id.find_next('td').get_text().strip()

    # Handling other rows
    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 2:
            key = columns[0].get_text().strip()
            value = columns[1].get_text().strip()
            mentor_details_dict[key] = value

            
    return mentor_details_dict