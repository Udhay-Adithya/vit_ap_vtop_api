from bs4 import BeautifulSoup

requests = {}
def parse_general_outing_requests(html: str) -> dict:
    requests = {}
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", id="BookingRequests")
    try:
        if table:
            rows = table.find_all("tr")[1:]
            for row in rows:
                cols = row.find_all("td")
                serial_number = cols[0].get_text().strip()
                booking_info = {
                    "registration_number": cols[1].get_text().strip(),
                    "place_of_visit": cols[2].get_text().strip(),
                    "purpose_of_visit": cols[3].get_text().strip(),
                    "from_date": cols[4].get_text().strip(),
                    "from_time": cols[5].get_text().strip(),
                    "to_date": cols[6].get_text().strip(),
                    "to_time": cols[7].get_text().strip(),
                    "leave_id": cols[8].get_text().strip(),
                    "action": cols[9].get_text().strip(),
                    "status": cols[10].get_text().strip(),
                }
                requests[serial_number] = booking_info

        return requests
    except Exception as e:
        return {"error" : e}