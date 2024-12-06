from bs4 import BeautifulSoup
import re

def parse_payment_receipts(html: str) -> list:
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("tr")[1:]
    payments = []
    # Pattern to extract `doDuplicateReceipt` parameter
    pattern = r"javascript:doDuplicateReceipt\('([^']*)'\);"
    
    for row in rows:
        cols = row.find_all("td")
        button = cols[4].find("button")
        onclick_value = button["onclick"] if button and "onclick" in button.attrs else None
        
        receipt_no = re.search(pattern, onclick_value).group(1) if onclick_value else "Unable to find receitNo"
        
        payment_info = {
            "receipt_number": cols[0].text.strip(),
            "date": cols[1].text.strip(),
            "amount": cols[2].text.strip(),
            "campus_code": cols[3].text.strip(),
            "payment_status": "Paid" if onclick_value else "Unknown",
            "receitNo": receipt_no,
        }
        
        payments.append(payment_info)
    
    return payments