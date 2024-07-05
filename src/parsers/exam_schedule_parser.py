from bs4 import BeautifulSoup

def parse_exam_schedule(html):
    soup = BeautifulSoup(html, 'html.parser')
    schedule_table = soup.find('table')

    if not schedule_table:
        print("Error: Could not find the schedule table in the HTML.")
        return

    rows = schedule_table.find_all('tr')
    exam_schedule = {}
    current_exam_type = None

    for row in rows:
        cells = row.find_all('td')
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
            "Course Code": values[1],
            "Course Title": values[2],
            "Type": values[3],
            "Registration Number": values[4],
            "Slot": values[5],
            "Date": values[6],
            "Session": values[7],
            "Reporting Time": values[8],
            "Exam Time": values[9],
            "Venue": values[10],
            "Room": values[11],
            "Marks": values[12]
        }

        # Add the entry to the dictionary under the current exam type
        exam_schedule[current_exam_type][values[0]] = exam_entry
        
    return exam_schedule