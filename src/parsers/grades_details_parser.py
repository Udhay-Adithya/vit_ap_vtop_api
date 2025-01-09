from bs4 import BeautifulSoup


def parse_grade_history(html : str) -> dict[str, str]:
    try: 
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', {'class': 'table table-hover table-bordered'})
        # Extract the row containing the desired data
        data_row = table.find('tbody').find('tr')
        # Extract the specific data points
        columns = data_row.find_all('td')
        grades : dict[str, str]= {
            'credits_registered': columns[0].get_text(strip=True),
            'credits_earned': columns[1].get_text(strip=True),
            'cgpa': columns[2].get_text(strip=True)
        }

        return grades
    except Exception as e:
        print(f"Error parsing grade history: {str(e)}")
        return {
            'credits_registered': "N/A",
            'credits_earned': "N/A",
            'cgpa': "N/A"
        }