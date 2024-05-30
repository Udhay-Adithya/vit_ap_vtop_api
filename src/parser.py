from bs4 import BeautifulSoup



data_list=[]
data_dict = {}

def attendence_parser(base):
	for table in base:
			base_list=table.get_text().split('\n')[18:]
			base_list = [item for item in base_list if item.strip()]

	# Iterate over the data_list in steps of 9 (since each subject has 9 entries in the list)
	for i in range(0, len(base_list), 9):
		# Split the second entry to get course code, name and type
		course_code, course_name_type = base_list[i+2].split(' - ', 1)
		course_name, course_type = course_name_type.rsplit(' - ', 1)
		
		# Split the third entry to get the unique ID and other details
		unique_id = base_list[i+3].split(' - ', 1)[0]
		
		# The fifth and sixth entries are the attended classes and total classes
		attended_classes = base_list[i+5]
		total_classes = base_list[i+6]
		
		# The seventh entry is the attendance percentage
		attendance_percentage = base_list[i+7].rstrip('%')
		
		# Add the data to the dictionary
		data_dict[unique_id] = {
			"CourseCode": course_code,
			"CourseName": course_name,
			"CourseType": course_type,
			"AttendedClasses": attended_classes,
			"TotalClasses": total_classes,
			"AttendancePercentage": attendance_percentage,
		}
	return data_dict



time_table_data = {'Tuesday':{},'Wednesday':{},'Thursday':{},'Friday':{},'Saturday':{}}
theory_timings=['DAY','TYPE','08:00 - 08:50', '09:00 - 09:50', '09:01 - 09:51', '10:00 - 10:50', '10:01 - 10:51', '11:00 - 11:50', '11:01 - 11:51', '12:00 - 12:50', '13:00 - 13:50', 'Lunch', '14:00 - 14:50', '14:01 - 14:51', '15:00 - 15:50', '15:01 - 15:51', '16:00 - 16:50', '16:01 - 16:51', '17:00 - 17:50', '18:00 - 18:50', '19:00 - 19:50']
lab_timings=['TYPE','08:00 - 08:50', '08:50 - 09:40', '08:51 - 09:41', '10:00 - 10:50', '10:01 - 10:51', '10:50 - 11:40', '10:51 - 11:41', '12:00 - 12:50', '12:50 - 13:30', 'Lunch', '14:00 - 14:50', '14:01 - 14:51', '14:50 - 15:40', '14:51 - 15:41', '16:00 - 16:50', '16:01 - 16:51', '16:50 - 17:40', '18:00 - 18:50', '18:50 - 19:30']
lst_table=[]

def get_course_info(html):
	soup = BeautifulSoup(html, 'html.parser')

    # Find all rows in the table
	rows = soup.find_all('tr')

    # Initialize an empty dictionary to store the courses and venues
	courses_dict = {}

    # Iterate through each row
	for row in rows:
        # Find the cells in the row
		cells = row.find_all('td')
        
        # Ensure the row has cells and there are at least 8 cells (to access Course and Venue)
		if cells and len(cells) >= 10:
			try:
                # Extract the course information from the respective cell
				course_p = cells[2].find('p')
				if course_p is not None:
					course = course_p.get_text().strip()

                    # Split the course information into the course code and course name
					course_code, course_name = course.split(' - ', 1)

                    # Extract the venue information from the respective cell
					venue_p = cells[7].find_all('p')
					for i in venue_p:
						if i is not None:
							venue = i.get_text().strip()
                    
                    # Store the course code, course name, and venue in the dictionary
					courses_dict[course_code] = {"Course Name": course_name, "Venue": venue}
			except Exception as e:
				print(f"An error occurred: {e}")
				continue
	return courses_dict




def update_timetable_with_course_info(timetable_data, courses_dict):
    for day, timeslots in timetable_data.items():
        for timeslot, course_info in timeslots.items():
            # Extract the course code from the course_info string
            course_code = course_info.split('-')[1]

            # If the course code is in the courses_dict, replace the course_info string with the course name and venue
            if course_code in courses_dict:
				# Determine if the class is a theory or lab class based on the timeslot
                course_type = 'ETH' if timeslot in theory_timings else 'ELA'
                timetable_data[day][timeslot] = {
                    "CourseName": courses_dict[course_code]["Course Name"],
                    "Venue": courses_dict[course_code]["Venue"],
                    "CourseCode": course_code,
                    "CourseType": course_type
                }
    return timetable_data
                


def parse_time_table(html):
	soup = BeautifulSoup(html, 'html.parser')

	# Find the table with id 'timeTableStyle'
	time_table = soup.find(id='timeTableStyle')
	if time_table:
		# Find all <tr> tags within the 'timeTableStyle' table starting from Tue
		tr_tags = time_table.find_all('tr')[4:]
		for tr_tag in tr_tags:
			tr_string = str(tr_tag.get_text(strip=False))
			# Split the string into lines
			lines = tr_string.split('\n')
			lines = list(filter(None, lines))
			lst_table.append(lines)
		
		#To access theory classes 	
		for day,line in zip(['Tuesday','Wednesday','Thursday','Friday','Saturday'],lst_table[::2]):
			for j in range(min(len(line), len(theory_timings))):
				if len(line[j])>8:
					time_table_data[day][theory_timings[j]] = line[j]

		#Labs
		for day,line in zip(['Tuesday','Wednesday','Thursday','Friday','Saturday'],lst_table[1::2]):
			for j in range(min(len(line), len(lab_timings))):
				if len(line[j])>8:
					time_table_data[day][lab_timings[j]] = line[j]

		for day in time_table_data:
			for time in list(time_table_data[day]):
				value=time_table_data[day][time]
				if len(value)<8:
					del time_table_data[day][time]
		return update_timetable_with_course_info(time_table_data,get_course_info(html))
	else:														
		print("No table with id 'timeTableStyle' found.")