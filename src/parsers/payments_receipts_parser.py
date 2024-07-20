import re
from bs4 import BeautifulSoup

def parse_payment_receipts(html) :
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')[1:]
    button_tag = soup.find('button')
    onclick_value = button_tag['onclick'] if button_tag else False
    pattern = r"javascript:doDuplicateReceipt\('([^']*)'\);"
    if onclick_value:
        data = {}
        for i, row in enumerate(rows, start=1):
            cols = row.find_all('td')
            data[i] = {
                'receipt_number': cols[0].text.strip(),
                'date': cols[1].text.strip(),
                'amount': cols[2].text.strip(),
                'campus_code': cols[3].text.strip(),
                'receitNo': re.search(pattern,cols[4].find('button')["onclick"]).group(1),
            }
        return data
    else:
        data = {}
        for i, row in enumerate(rows, start=1):
            cols = row.find_all('td')
            data[i] = {
                'receipt_number': cols[0].text.strip(),
                'date': cols[1].text.strip(),
                'amount': cols[2].text.strip(),
                'campus_code': cols[3].text.strip(),
                'receitNo': "Unable to find receitNo",
            }
            return data