from bs4 import BeautifulSoup
import json

html="""<tbody><tr>
										<td style="background-color: #aba6bf; font-weight: bold;"> Faculty ID</td>
										<td style="background-color: #f2dede;">70583</td>
 										<td style="background-color: #f2dede;" rowspan="9"> 
 											<img src="assets/img/navatar.png" class="img-rounded" alt="Image Not Available" width="150" height="180" style="border: solid 2px #3c8dbc;">
 										</td>
									</tr>
									<tr>
										<td style="background-color: #aba6bf; font-weight: bold;"> Faculty Name</td>
										<td style="background-color: #f2dede;">DR.SANZIOU BORO </td>
 									</tr>
									<tr>
										<td style="background-color: #aba6bf; font-weight: bold;">Faculty Designation</td>
										<td style="background-color: #f2dede;">Assistant Professor Sr. Grade-2</td>
 									</tr>
 									 <tr>
										<td style="background-color: #aba6bf; font-weight: bold;"> School</td>
										<td style="background-color: #f2dede;">School of Social Sciences and Humanities</td>
 									</tr>
									<tr>
										<td style="background-color: #aba6bf; font-weight: bold;"> Cabin</td>
										<td style="background-color: #f2dede;">107-AB1</td>
 									</tr>
									<tr>
										<td style="background-color: #aba6bf;font-weight: bold;">Faculty Department</td>
										<td style="background-color: #f2dede;">Department of Languages</td>
 									</tr>
									<tr>
										<td style="background-color: #aba6bf;font-weight: bold;"> Faculty Email</td>
										<td style="background-color: #f2dede;">sanziou.b@vitap.ac.in</td>
 									</tr>
 									<tr>
										<td style="background-color: #aba6bf;font-weight: bold;">Faculty intercom</td>
										<td style="background-color: #f2dede;"></td>
 									</tr>
 									
 									<tr>
										<td style="background-color: #aba6bf;font-weight: bold;">Faculty Mobile Number</td>
										<td style="background-color: #f2dede;">7044403633</td>
 									</tr>
								</tbody>"""

soup = BeautifulSoup(html, "html.parser")
mentor_data = soup.find_all('td')
mentor_details_dict = {}


# Handling 'Faculty ID' separately
faculty_id = soup.find('td', string=' Faculty ID')
if faculty_id:
    mentor_details_dict[faculty_id.get_text().strip()] = faculty_id.find_next('td').get_text().strip()

# Handling other rows
for row in soup.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) == 2:
        key = columns[0].get_text().strip()
        value = columns[1].get_text().strip()
        mentor_details_dict[key] = value

with open('mentor_details.json', 'w') as json_file:
    json.dump(mentor_details_dict, json_file, indent=4)