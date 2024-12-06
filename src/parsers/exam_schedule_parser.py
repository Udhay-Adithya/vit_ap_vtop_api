from typing import List, Dict
from bs4 import BeautifulSoup
from collections import defaultdict


def parse_exam_schedule(html: str) -> List[Dict] | dict:
    soup = BeautifulSoup(html, "html.parser")
    schedule_table = soup.find("table")

    if not schedule_table:
        return {"error": "No timetable found"}

    rows = schedule_table.find_all("tr")
    exam_schedule = defaultdict(list)
    current_exam_type = None

    for row in rows:
        cells = row.find_all("td")
        values = [cell.text.strip() for cell in cells]

        # Skip rows that don't contain enough values or are headers
        if len(values) == 1:
            current_exam_type = values[0]
            continue
        elif len(values) < 13 or "S.No." in values:
            continue

        # Construct the data dictionary
        exam_entry = {
            "serial_number": values[0],
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

        # Add the entry to the list under the current exam type
        if current_exam_type:
            exam_schedule[current_exam_type].append(exam_entry)

    # Convert defaultdict to a list of dictionaries
    result = [
        {
            "exam_type": exam_type,
            "subjects": subjects
        }
        for exam_type, subjects in exam_schedule.items()
    ]

    return result