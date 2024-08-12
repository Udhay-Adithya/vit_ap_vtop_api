from bs4 import BeautifulSoup


def parse_print_payment_receipt_page(html: str, receipts: dict, index: int) -> dict:
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Initialize a dictionary to store the extracted data
    details = {}
    try:
        # Extract receipt details
        receipt_details = soup.find("table", class_="table noborder")
        rows = receipt_details.find_all("tr")
        for row in rows:
            headers = row.find_all("th")
            cols = row.find_all("td")
            if len(headers) > 1 and len(cols) > 1:
                if "Receipt Number" in headers[0].text.strip():
                    details["receipt_number"] = cols[0].text.strip()
                    details["name"] = cols[1].text.strip()
                if "Receipt Date" in headers[0].text.strip():
                    details["receipt_date"] = cols[0].text.strip()
                    details["application_number/register_number"] = cols[1].text.strip()
                if "Payment Year" in headers[0].text.strip():
                    details["payment_year"] = cols[0].text.strip()
                    details["campus"] = cols[1].text.strip()
                if "Program Name" in headers[0].text.strip():
                    details["program_name"] = cols[0].text.strip()

        # Extract hostel fees details
        details["fee"] = []
        hostel_fees_table = soup.find_all("table", class_="table")[1]
        rows = hostel_fees_table.find_all("tr")[1:]  # Skip the header row
        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 4:
                fee_details = {
                    "serial_number": cols[0].text.strip(),
                    "invoice_number": cols[1].text.strip(),
                    "description": cols[2].text.strip(),
                    "amount": cols[3].text.strip(),
                }
                details["fee"].append(fee_details)

        # Extract grand total and amount in words
        grand_total_div = soup.find("div", class_="text text-primary text-right")
        if grand_total_div:
            details["grand_total"] = grand_total_div.text.strip().split(":")[1].strip()
        amount_in_words_div = soup.find(
            "div", class_="text", text=lambda t: t and t.startswith("(Rupees")
        )
        if amount_in_words_div:
            details["amount_in_words"] = amount_in_words_div.text.strip()

        # Extract payment details
        details["payment_details"] = []
        payment_table = soup.find_all("table", class_="table")[2]
        rows = payment_table.find_all("tr")[1:]  # Skip the header row
        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 4:
                payment_detail = {
                    "payment_mode": cols[0].text.strip(),
                    "bank_name": cols[1].text.strip(),
                    "dd_no/online_transaction_id.": cols[2].text.strip(),
                    "amount": cols[3].text.strip(),
                }
                details["payment_details"].append(payment_detail)
        receipts[index]["details"] = details
        return receipts
    except Exception as e:
        return {"error": f"Unknown error occured while fetching payments : {e}"}
