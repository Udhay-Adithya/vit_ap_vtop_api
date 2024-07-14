from bs4 import BeautifulSoup

def parse_payment_receipts(html) :
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')[1:]

    data = {}
    for i, row in enumerate(rows, start=1):
        cols = row.find_all('td')
        data[i] = {
            'receipt_number': cols[0].text.strip(),
            'date': cols[1].text.strip(),
            'amount': float(cols[2].text.strip()),
            'campus_code': cols[3].text.strip()
        }
    return data