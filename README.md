<br />
<p align="center">
    <img src="public/Final_Icon_512x512.png" width="100" height="100" style="margin-right: 60px;"> 
    <img src="public/vitaplogo.png" width="322" height="100"> 
</p>
<br>
<br>

<p align="center">
    <a href="https://github.com/Udhay-Adithya/vit_ap_vtop_api">
    <img src="https://img.shields.io/github/stars/Udhay-Adithya/vit_ap_vtop_api?style=social" alt="License: MIT">
    </a>
    <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
    </a>
    <img src="https://img.shields.io/badge/Version-0.1.5-blue.svg" alt="Version 0.1.5">
    <a href="https://github.com/Udhay-Adithya/vitap-vtop-client/issues">
    <img src="https://img.shields.io/github/issues/Udhay-Adithya/vit_ap_vtop_api" alt="License: MIT">
    </a>
</p>
<br>

This API, built with FastAPI, serves as a wrapper for the [vitap-vtop-client](https://github.com/Udhay-Adithya/vitap-vtop-client) library. It allows students of VIT-AP to programmatically access their academic information such as profile, attendance, timetable, exam schedules, marks, and more from the VIT-AP VTOP Portal.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Endpoints](#endpoints)
6. [Example Usage](#example-usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Future Updates](#future-updates)
10. [Companion App](#companion-app)

## Overview
The VIT-AP VTOP API is designed to help students access their academic information programmatically. It is built using Python with FastAPI and relies on the [`vitap-vtop-client`](https://github.com/Udhay-Adithya/vitap-vtop-client) library to scrape data from the [V-TOP](https://vtop.vitap.ac.in/vtop/) Portal using the user’s credentials.

## Features
- **User Profile Info**: Retrieve detailed student profile information.
- **Attendance**: Get attendance records for a specified semester.
- **Biometric Log**: Access daily biometric (in/out) logs.
- **Time Table**: Fetch the class timetable for a given semester.
- **Grade History**: Retrieve academic grade history, including CGPA and credit details.
- **Mentor Details**: Get information about the assigned faculty mentor.
- **Exam Schedule**: Access the schedule for upcoming examinations for a semester.
- **Marks Details**: Fetch marks obtained in various assessments for a semester.
- **Outing Requests Status**: Retrieve the status of submitted general and weekend outing requests.

## Installation
This project uses Poetry for dependency management.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Udhay-Adithya/vit_ap_vtop_api.git
    cd vit_ap_vtop_api
    ```

2.  **Install dependencies using Poetry**:
    ```bash
    poetry install
    ```

For a detailed development setup, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Running the Application
To run the FastAPI application locally for development:

1.  Ensure you have an `.env` file configured with necessary environment variables (e.g., `API_KEY`).
2.  From the project root directory, run:
    ```bash
    poetry run uvicorn src.main:app --reload
    ```
    The application will typically be available at `http://127.0.0.1:8000`.

## Endpoints

All API endpoints are documented in detail in the [DOCS.md](DOCS.md) file. This includes information on request parameters, response formats, and authentication.

## Example Usage
### Fetch All Student Data
Here's an example of how to fetch comprehensive data for a student using Python's `requests` library. Remember to replace placeholders with actual values and include your `API-KEY` in the headers.

```python
import requests
import json

api_url = 'http://127.0.0.1:8000/student/all_data'
api_key = 'YOUR_API_KEY' # Replace with your actual API key

payload = {
    "registration_number": "YOUR_REGISTRATION_NUMBER", # e.g., "21BCE0001"
    "password": "YOUR_VTOP_PASSWORD",
    "sem_sub_id": "YOUR_SEMESTER_ID" # e.g., "VL20232405" for Fall Semester 2023-24
}

headers = {
    'X-API-KEY': api_key,
    'Content-Type': 'application/json'
}

try:
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
    data = response.json()
    print(json.dumps(data, indent=2))
except requests.exceptions.HTTPError as errh:
    print(f"Http Error: {errh}")
    print(f"Response content: {response.text}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Oops: Something Else: {err}")
    if response:
        print(f"Response content: {response.text}")

```

## Contributing
Contributions are welcome! Please see [CONTRIBUTING.md](/CONTRIBUTING.md) for guidelines.

## License
This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.

## Future Updates
We are committed to improving this API and the companion app. Future updates will include new features, bug fixes, and performance improvements.

## Companion App
I have also developed a companion app for this API. The VITAP Student App provides a user-friendly interface for accessing your academic information on your mobile device. You can find the app repository [here](https://github.com/Udhay-Adithya/vit_ap_student_app/).

We encourage users to try out the app and provide feedback. Future updates will enhance both the API and the app to better serve the needs of VIT-AP students.

---

Thank you for using the VIT-AP VTOP API! If you have any questions or need further assistance, feel free to open an issue on GitHub.
