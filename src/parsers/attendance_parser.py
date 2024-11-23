from bs4 import BeautifulSoup

def parse_attendance(html: str) -> dict:
    try:
        soup = BeautifulSoup(html, "html.parser")
        data_dict = {}
        
        # Find all rows in the table
        rows = soup.find('table', id='AttendanceDetailDataTable').find_all('tr')[1:]  # Skip header row
        
        for row in rows:
            # Get all cells in the row
            cells = row.find_all('td')
            
            # Split course details
            course_details = cells[2].get_text(strip=True)
            course_code, course_name_type = course_details.split(' - ', 1)
            course_name, course_type = course_name_type.rsplit(' - ', 1)
            
            # Get unique ID from class detail
            unique_id = cells[3].get_text(strip=True).split(' - ', 1)[0]
            
            # Get attendance details
            attended_classes = cells[5].get_text(strip=True)
            total_classes = cells[6].get_text(strip=True)
            attendance_percentage = cells[7].get_text(strip=True).rstrip('%')
            
            # Create dictionary entry
            data_dict[unique_id] = {
                "course_code": course_code,
                "course_name": course_name,
                "course_type": course_type,
                "attended_classes": attended_classes,
                "total_classes": total_classes,
                "attendance_percentage": attendance_percentage,
            }
            
        return data_dict
    except Exception as e:
        return {"error": "Failed to parse attendance data: " + str(e)}