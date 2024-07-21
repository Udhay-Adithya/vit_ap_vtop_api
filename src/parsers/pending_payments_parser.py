from bs4 import BeautifulSoup

def pending_payments_parser(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    
    # Initialize the dictionary with empty lists
    data = {}
    
    # Iterate over the table rows, skipping the header row
    if table:
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            data['s_no'] = cols[0].text.strip()
            data['fprefno'] = cols[1].text.strip()
            data['fees_heads']=cols[2].text.strip()
            data['end_date']=cols[3].text.strip()
            data['amount']=cols[4].text.strip()
            data['fine']=cols[5].text.strip()
            data['total_amount']=cols[6].text.strip()
            data['payment_status']='Unpaid'
        return data
    else :
        message = soup.find(text="There is no payment dues in your account!")
        if message is not None:
            return message
        else :
            return "Unable to find payment dues"