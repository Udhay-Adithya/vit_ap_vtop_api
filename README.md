# VIT-AP VTOP API

Welcome to the VIT-AP VTOP API documentation. This API allows students of VIT-AP to fetch various details such as attendance, biometric logs, exam schedules, HOD details, mentor details, time table, user profile information, and more from the VIT-AP VTOP Portal.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Endpoints](#endpoints)
5. [Example Usage](#example-usage)
6. [Contributing](#contributing)
7. [License](#license)
8. [Future Updates](#future-updates)
9. [Companion App](#companion-app)

## Overview
The VIT-AP VTOP API is designed to help students access their academic information programmatically. It is built using Python and is hosted on [Fly.io](https://fly.io/). The API scrapes data from the [V-TOP](https://vtop.vitap.ac.in/vtop/) Portal using the user’s credentials.

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

For a detailed setup information see [CONTRIBUTING.md](/CONTRIBUTING.md)


## Endpoints

Refer to the main documentation [`DOCS.md`](/DOCS.md) for all endpoint related information.

## Example Usage
### Login and Fetch Attendance
```python
import requests

# Login and fetch all data
url = 'http://127.0.0.1:8000/login/getalldata'
payload = {
    "username": "your_username",
    "password": "your_password",
    "semSubID": "your_semester_ID"
}
response = requests.post(url, data=payload)
data = response.json()
print(data)
```

## Contributing
Contributions are welcome! Please see [CONTRIBUTING.md](/CONTRIBUTING.md) for guidelines.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Future Updates
We are committed to improving this API and the companion app. Future updates will include new features, bug fixes, and performance improvements.

## Companion App
I have also developed a companion app for this API. The VITAP Student App provides a user-friendly interface for accessing your academic information on your mobile device. You can find the app repository [here](https://github.com/Udhay-Adithya/vit_ap_student_app/).

We encourage users to try out the app and provide feedback. Future updates will enhance both the API and the app to better serve the needs of VIT-AP students.

---

Thank you for using the VIT-AP VTOP API! If you have any questions or need further assistance, feel free to open an issue on GitHub.
