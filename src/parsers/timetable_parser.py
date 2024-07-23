from bs4 import BeautifulSoup

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
            print(course_info)
            # Extract the course code from the course_info string
            try:
               course_code = course_info.split('-')[1]
            except Exception as e:
                course_code= "N/A"
            print(course_code)
            # If the course code is in the courses_dict, replace the course_info string with the course name and venue
            if course_code in courses_dict:
				# Determine if the class is a theory or lab class based on the timeslot
                course_type = 'ETH' if timeslot in theory_timings else 'ELA'
                timetable_data[day][timeslot] = {
                    "course_name": courses_dict[course_code]["Course Name"],
                    "venue": courses_dict[course_code]["Venue"],
                    "course_code": course_code,
                    "course_type": course_type
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
		return "Unable to find timetable."