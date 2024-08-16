from bs4 import BeautifulSoup

requests = {}
def parse_weekend_outing_requests(html: str) -> dict:
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
                    "hostel_block": cols[2].get_text().strip(),
                    "room_number": cols[3].get_text().strip(),
                    "place_of_visit": cols[4].get_text().strip(),
                    "purpose_of_visit": cols[5].get_text().strip(),
                    "time": cols[6].get_text().strip(),
                    "contact_number": cols[7].get_text().strip(),
                    "parent_contact_number": cols[8].get_text().strip(),
                    "date": cols[9].get_text().strip(),
                    "booking_id": cols[10].get_text().strip(),
                    "action": cols[11].get_text().strip(),
                    "status": cols[12]
                    .get_text()
                    .replace("\n", " ")
                    .replace("\t", "")
                    .strip(),
                }
                requests[serial_number] = booking_info

        return requests
    except Exception as e:
        return {"error" : e}