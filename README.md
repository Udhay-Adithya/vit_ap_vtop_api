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
    <img src="https://img.shields.io/badge/Version-0.3.0-blue.svg" alt="Version 0.3.0">
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

All 33 endpoints are documented at **[udhay-adithya.github.io/vit_ap_vtop_api](https://udhay-adithya.github.io/vit_ap_vtop_api/)**, generated from the service's own OpenAPI schema so it cannot drift from the routes. A running instance serves the same thing interactively at `/docs`.

Start with the [authentication guide](https://udhay-adithya.github.io/vit_ap_vtop_api/guide/authentication.html): credentials are sent once to `/auth/login`, and every call after that carries the session it returns.

## Example Usage
### Fetch All Student Data

Credentials go to `/auth/login` once. Everything after that carries the session it
returns — which is both far faster and the only way the OTP flow can work, since
VTOP raises the challenge on one request and receives the answer on the next.

```python
import requests

BASE = "http://127.0.0.1:8000"
HEAD = {"X-API-Key": "YOUR_API_KEY", "Content-Type": "application/json"}

# 1. log in once
login = requests.post(f"{BASE}/auth/login", headers=HEAD, json={
    "registration_number": "YOUR_REGISTRATION_NUMBER",
    "password": "YOUR_VTOP_PASSWORD",
}).json()

# VTOP asks for an OTP after inactivity, or from an IP it has not seen before.
# That is a normal outcome rather than an error, so it comes back as a 200.
if login["status"] == "otp_required":
    otp = input("OTP sent to your registered email: ")
    login = requests.post(f"{BASE}/auth/verify_otp", headers=HEAD, json={
        "otp_challenge": login["otp_challenge"],
        "otp": otp,
    }).json()

session = login["session"]

# 2. ask VTOP which semesters exist rather than hardcoding an id: an unknown one
#    comes back empty rather than failing, so a stale id fails silently.
semesters = requests.post(f"{BASE}/student/semesters", headers=HEAD,
                          json={"session": session}).json()
sem_id = semesters["semesters"][0]["id"]

# 3. every data call carries the session
data = requests.post(f"{BASE}/student/all_data", headers=HEAD,
                     json={"session": session, "sem_sub_id": sem_id})

if data.status_code == 401:
    # the session expired; log in again, which may need another OTP
    ...

print(data.json())
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
