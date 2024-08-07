from bs4 import BeautifulSoup


def parse_exam_schedule(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    schedule_table = soup.find("table")

    if not schedule_table:
        return {"error ": "No timetable found"}

    rows = schedule_table.find_all("tr")
    exam_schedule = {}
    current_exam_type = None

    for row in rows:
        cells = row.find_all("td")
        values = [cell.text.strip() for cell in cells]

        # Skip rows that don't contain enough values or are headers
        if len(values) == 1:
            current_exam_type = values[0]
            exam_schedule[current_exam_type] = {}
            continue
        elif len(values) < 13 or "S.No." in values:
            continue

        # Construct the data dictionary
        exam_entry = {
            "course_code": values[1],
            "course_title": values[2],
            "type": values[3],
            "registration_number": values[4],
            "slot": values[5],
            "date": values[6],
            "session": values[7],
            "reporting_time": values[8],
            "exam_time": values[9],
            "venue": values[10],
            "seat_location": values[11],
            "seat_number": values[12],
        }

        # Add the entry to the dictionary under the current exam type
        exam_schedule[current_exam_type][values[0]] = exam_entry

    return exam_schedule
