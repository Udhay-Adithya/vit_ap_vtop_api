from bs4 import BeautifulSoup

def parse_payment_receipts(html) :
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')[1:]

    data = {}
    for i, row in enumerate(rows, start=1):
        cols = row.find_all('td')
        data[i] = {
            'RECEIPT NUMBER': cols[0].text.strip(),
            'DATE': cols[1].text.strip(),
            'AMOUNT': float(cols[2].text.strip()),
            'CAMPUS CODE': cols[3].text.strip()
        }
    return data