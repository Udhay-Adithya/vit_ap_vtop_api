# VIT-AP VTOP API

Welcome to the VIT-AP VTOP API documentation. This API allows students of VIT-AP to fetch various details such as attendance, biometric logs, exam schedules, HOD details, mentor details, time table, user profile information, and more from the VIT-AP VTOP Portal.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Endpoints](#endpoints)
6. [Examples](#examples)
7. [Error Handling](#error-handling)
8. [Contributing](#contributing)
9. [License](#license)
10. [Future Updates](#future-updates)
11. [Companion App](#companion-app)

## Overview
The VIT-AP VTOP API is designed to help students access their academic information programmatically. It is built using Python and is hosted on [Fly.io](https://fly.io/). The API scrapes data from the VTOP system using the user’s credentials.

## Features
- **Attendance**: Fetch attendance details for the user.
- **Biometric Log**: Retrieve biometric logs for the user.
- **Exam Schedule**: Get the exam schedule for the user.
- **HOD Details**: Access Head of Department details.
- **Mentor Details**: Access mentor details.
- **Time Table**: Get the user's class timetable.
- **User Profile Info**: Retrieve the user's profile information.

## Installation
To use the API, clone the repository and install the required dependencies.

```bash
git clone https://github.com/Udhay-Adithya/VIT-AP-VTOP-API.git
cd VIT-AP-VTOP-API
pip install -r requirements.txt
```

## Usage
Run the API server locally:

```bash
python app.py
```

Deploy the API using [Fly.io](https://fly.io/). Follow the Fly.io documentation for deployment steps.

## Endpoints
### General
- **GET /**
  - Description: Returns a welcome message.
  - Response:
    ```text
    You can access this API on Github
    ```

### Captcha
- **GET /getCaptcha**
  - Description: Fetches a captcha image required for login.
  - Response: Captcha image.

### Login and Data Retrieval
- **POST /login/getalldata**
  - Description: Logs in and retrieves profile, attendance, and timetable data.
  - Request Body:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "semSubID": "your_semSubID"
    }
    ```
  - Response:
    ```json
    {
      "profile": {...},
      "attendance": {...},
      "timetable": {...}
    }
    ```

### Individual Data Retrieval
- **POST /login/profile**
  - Description: Logs in and retrieves user profile information.
  - Request Body:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - Response:
    ```json
    {
      "profile": {...}
    }
    ```

- **POST /login/timetable**
  - Description: Logs in and retrieves the class timetable.
  - Request Body:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "semSubID": "your_semSubID"
    }
    ```
  - Response:
    ```json
    {
      "timetable": {...}
    }
    ```

- **POST /login/attendance**
  - Description: Logs in and retrieves attendance details.
  - Request Body:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "semSubID": "your_semSubID"
    }
    ```
  - Response:
    ```json
    {
      "attendance": {...}
    }
    ```

- **POST /login/biometric**
  - Description: Logs in and retrieves biometric logs for a specific date.
  - Request Body:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "date": "yyyy-mm-dd"
    }
    ```
  - Response:
    ```json
    {
      "biometric_log": {...}
    }
    ```

## Examples
### Login and Fetch Attendance
```python
import requests

# Login and fetch all data
url = 'https://your-api-url.com/login/getalldata'
payload = {
    "username": "your_username",
    "password": "your_password",
    "semSubID": "your_semester_ID"
}
response = requests.post(url, data=payload)
data = response.json()
print(data)
```

## Error Handling
The API returns appropriate HTTP status codes and error messages for invalid requests. Common errors include:
- `400 Bad Request`: Invalid request format.
- `401 Unauthorized`: Authentication failed.
- `403 Forbidden`: Access denied.
- `404 Not Found`: Resource not found.
- `500 Internal Server Error`: Server error.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project’s coding standards and includes relevant tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Future Updates
We are committed to improving this API and the companion app. Future updates will include new features, bug fixes, and performance improvements.

## Companion App
I have also developed a companion app for this API. The VITAP Student App provides a user-friendly interface for accessing your academic information on your mobile device. You can find the app repository [here](https://github.com/Udhay-Adithya/VITAP-Student-App/).

We encourage users to try out the app and provide feedback. Future updates will enhance both the API and the app to better serve the needs of VIT-AP students.

---

Thank you for using the VIT-AP VTOP API! If you have any questions or need further assistance, feel free to open an issue on GitHub.
