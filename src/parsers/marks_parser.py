from bs4 import BeautifulSoup

data = []


def marks_parser(html: str) -> (list | dict[str, str]) :
	soup = BeautifulSoup(html, "html.parser")
	try:
			# Parse the HTML using BeautifulSoup
			soup = BeautifulSoup(html, "html.parser")
			# Find the main table with the class 'customTable'
			main_table = soup.find("table", class_="customTable")
			# Find all the rows in the table, ignoring the first row (header)
			rows = main_table.find_all("tr", class_="tableContent")
			subjects = []
			for i in range(0, len(rows), 2):
				# Parse basic info from the even-numbered row
				basic_info_row = rows[i].find_all("td")
				# logging.critical(basic_info_row)
				# Extract the basic info fields
				basic_info = {
					"serial_number": basic_info_row[0].text.replace("\n", ""),
					"class_id": basic_info_row[1].text.strip("\n"),
					"course_code": basic_info_row[2].text.strip("\n"),
					"course_title": basic_info_row[3].text.strip("\n"),
					"course_type": basic_info_row[4].text.strip("\n"),
					"course_system": basic_info_row[5].text.strip("\n"),
					"faculty": basic_info_row[6].text.strip("\n"),
					"slot": basic_info_row[7].text.strip("\n"),
				}
				if i + 1 < len(rows):
					detailed_info_row = rows[i + 1]
					nested_table = detailed_info_row.find("table", class_="customTable-level1")
					detailed_info = []
					if nested_table:
						nested_rows = nested_table.find_all("tr")[1:]  # Skip the header row
						for nested_row in nested_rows:
							nested_cols = nested_row.find_all("td")
							detail = {
								"serial_number": nested_cols[0].text.strip("\\n"),
								"mark_title": nested_cols[1].text.strip(r"\n"),
								"max_mark": nested_cols[2].text.strip("\n"),
								"weightage": nested_cols[3].text.strip("\n"),
								"status": nested_cols[4].text.strip("\n"),
								"scored_mark": nested_cols[5].text.strip("\n"),
								"weightage_mark": nested_cols[6].text.strip("\n"),
								"remark": nested_cols[7].text.strip("\n"),
							}
							detailed_info.append(detail)
					# Add the detailed info to the basic info
					basic_info["details"] = detailed_info
					# Append the subject info to the final list
				subjects.append(basic_info)
			return subjects
	except Exception as e:
		span_red = soup.find(
        "span", {"style": "font-size: 20px; color: red; text-align: center;"}
	    )	
		print(str(e))
		if span_red:
			return {'error' : span_red.get_text()}
		else:
			return {'error' : str(e)}