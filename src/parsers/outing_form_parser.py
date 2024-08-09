from bs4 import BeautifulSoup


def parse_outing_form(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    outing_info = {}
    outing_info['register_number'] = soup.find('input', {'id': 'regNo'})['value']
    outing_info['name'] = soup.find('input', {'id': 'name'})['value']
    outing_info['application_no'] = soup.find('input', {'id': 'applicationNo'})['value']
    outing_info['gender'] = soup.find('input', {'id': 'gender'})['value']
    outing_info['hostel_block'] = soup.find('input', {'id': 'hostelBlock'})['value']
    outing_info['room_number'] = soup.find('input', {'id': 'roomNo'})['value']
    outing_info['parent_contact_number'] = soup.find('input', {'id': 'parentContactNumber'})['value']

    return outing_info