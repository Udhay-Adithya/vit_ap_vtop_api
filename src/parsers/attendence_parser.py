from bs4 import BeautifulSoup

data_list=[]
data_dict = {}

def parse_attendence(base):
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
			"course_code": course_code,
			"course_name": course_name,
			"course_type": course_type,
			"attended_classes": attended_classes,
			"total_classes": total_classes,
			"attendance_percentage": attendance_percentage,
		}
	return data_dict
