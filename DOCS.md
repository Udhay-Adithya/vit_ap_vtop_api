# VIT-AP VTOP API Documentation

Welcome to the detailed documentation for the VIT-AP VTOP API. This API, built with FastAPI, provides programmatic access to student academic information from the VIT-AP VTOP Portal. This document outlines all available endpoints, request parameters, response formats, and authentication requirements.

## Table of Contents
1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [General Endpoints](#general-endpoints)
4. [Student Data Endpoints](#student-data-endpoints)
   - [Get All Student Data](#1-get-all-student-data)
   - [Get User Profile](#2-get-user-profile)
   - [Get Attendance](#3-get-attendance)
   - [Get Biometric Log](#4-get-biometric-log)
   - [Get Timetable](#5-get-timetable)
   - [Get Grade History](#6-get-grade-history)
   - [Get Mentor Details](#7-get-mentor-details)
   - [Get Exam Schedule](#8-get-exam-schedule)
   - [Get Marks](#9-get-marks)
   - [Get General Outing Requests](#10-get-general-outing-requests)
   - [Get Weekend Outing Requests](#11-get-weekend-outing-requests)
5. [Error Handling](#error-handling)

## Introduction
The VIT-AP VTOP API is a FastAPI wrapper around the `vitap-vtop-client` library. It allows authenticated users to fetch various academic details by providing VTOP credentials. All endpoints requiring VTOP login first authenticate with the VTOP system and then retrieve the requested information.

The API interactive documentation (Swagger UI) is typically available at `/docs` and ReDoc at `/redoc` when the application is running.

## Authentication
Two levels of authentication are in place:

1.  **API Key**: All requests to this API must include an `API-KEY` in the request headers.
    ```
    API-KEY: YOUR_API_KEY
    ```
    Requests without a valid API key will result in a `401 Unauthorized` error. The API key is configured via an environment variable (e.g., `API_SECRET_KEY`) on the server.

2.  **VTOP Credentials**: For endpoints under the `/student/` path, user VTOP credentials (`registration_number` and `password`) are required in the JSON request body to authenticate with the VTOP portal.

## General Endpoints

### 1. Welcome Message
- **GET /**
  - **Description**: Returns a welcome message and a link to the API documentation.
  - **Response** (`application/json`):
    ```json
    {
      "message": "Welcome to VITAP VTOP API. Check out /docs to get started."
    }
    ```

## Student Data Endpoints
All endpoints listed below are `POST` requests, prefixed with `/student/`, and require both an `API-KEY` in headers and VTOP credentials (`registration_number`, `password`) in the JSON request body. Specific parameters like `sem_sub_id` or `date` are also part of the request body where applicable.

### 1. Get All Student Data
- **POST /student/all_data**
  - **Description**: Fetches a comprehensive set of student data, including profile, attendance, timetable, exam schedule, grade history, and marks for the specified semester.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password",
      "sem_sub_id": "your_semester_ID"
    }
    ```
  - **Response** (`application/json`):
    ```json
    {
      "profile": { /* StudentProfileModel structure from vitap_vtop_client.profile */ },
      "attendance": [ /* List of AttendanceModel structure from vitap_vtop_client.attendance */ ],
      "timetable": { /* TimetableModel structure from vitap_vtop_client.timetable */ },
      "exam_schedule": { /* ExamScheduleModel structure from vitap_vtop_client.exam_schedule */ },
      "grade_history": { /* GradeHistoryModel structure from vitap_vtop_client.grade_history */ },
      "marks": { /* MarksModel structure from vitap_vtop_client.marks */ }
    }
    ```

### 2. Get User Profile
- **POST /student/profile**
  - **Description**: Fetches the student's profile information.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password"
    }
    ```
  - **Response** (`application/json`):
    ```json
    { /* StudentProfileModel structure from vitap_vtop_client.profile */ }
    ```

### 3. Get Attendance
- **POST /student/attendance**
  - **Description**: Fetches attendance data for the specified semester.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password",
      "sem_sub_id": "your_semester_ID"
    }
    ```
  - **Response** (`application/json`):
    ```json
    [
      { /* AttendanceModel structure from vitap_vtop_client.attendance */ }
    ]
    ```

### 4. Get Biometric Log
- **POST /student/biometric**
  - **Description**: Fetches biometric (entry/exit) logs for a specific date.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password",
      "date": "YYYY-MM-DD"
    }
    ```
  - **Response** (`application/json`):
    ```json
    [
      { /* BiometricModel structure from vitap_vtop_client.biometric */ }
    ]
    ```

### 5. Get Timetable
- **POST /student/timetable**
  - **Description**: Fetches the class timetable for the specified semester.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password",
      "sem_sub_id": "your_semester_ID"
    }
    ```
  - **Response** (`application/json`):
    ```json
    { /* TimetableModel structure from vitap_vtop_client.timetable */ }
    ```

### 6. Get Grade History
- **POST /student/grade_history**
  - **Description**: Fetches the student's grade history (CGPA, credits registered/earned).
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password"
    }
    ```
  - **Response** (`application/json`):
    ```json
    { /* GradeHistoryModel structure from vitap_vtop_client.grade_history */ }
    ```

### 7. Get Mentor Details
- **POST /student/mentor**
  - **Description**: Fetches details of the student's assigned mentor.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password"
    }
    ```
  - **Response** (`application/json`):
    ```json
    { /* MentorModel structure from vitap_vtop_client.mentor */ }
    ```

### 8. Get Exam Schedule
- **POST /student/exam_schedule**
  - **Description**: Fetches the exam schedule for the specified semester.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password",
      "sem_sub_id": "your_semester_ID"
    }
    ```
  - **Response** (`application/json`):
    ```json
    { /* ExamScheduleModel structure from vitap_vtop_client.exam_schedule */ }
    ```

### 9. Get Marks
- **POST /student/marks**
  - **Description**: Fetches all marks for the specified semester.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password",
      "sem_sub_id": "your_semester_ID"
    }
    ```
  - **Response** (`application/json`):
    ```json
    { /* MarksModel structure from vitap_vtop_client.marks */ }
    ```

### 10. Get General Outing Requests
- **POST /student/general_outing_requests**
  - **Description**: Fetches all previously submitted General Outing requests.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password"
    }
    ```
  - **Response** (`application/json`):
    ```json
    { /* GeneralOutingModel structure from vitap_vtop_client.outing */ }
    ```

### 11. Get Weekend Outing Requests
- **POST /student/weekend_outing_requests**
  - **Description**: Fetches all previously submitted Weekend Outing requests.
  - **Request Body** (`application/json`):
    ```json
    {
      "registration_number": "your_registration_number",
      "password": "your_vtop_password"
    }
    ```
  - **Response** (`application/json`):
    ```json
    { /* WeekendOutingModel structure from vitap_vtop_client.outing */ }
    ```

## Error Handling
The API returns appropriate HTTP status codes and error messages for invalid requests or server-side issues. Common errors include:
- `400 Bad Request`: Invalid request format, missing parameters, or validation errors from Pydantic models. The response body will often contain details about the validation error.
- `401 Unauthorized`: Authentication failed (Invalid or missing `API-KEY`).
- `403 Forbidden`: VTOP authentication failed (e.g., invalid `registration_number` or `password`, CAPTCHA issues, account locked, or other VTOP-side errors). The response detail may provide more specific information from the `vitap-vtop-client` library.
- `422 Unprocessable Entity`: If the request body is syntactically correct JSON but fails Pydantic model validation (e.g., wrong data types).
- `500 Internal Server Error`: An unexpected error occurred on the server or within the `vitap-vtop-client` library during scraping.

Error responses are typically in JSON format:
```json
{
  "detail": "Error message or validation details"
}
```
For VTOP client errors (often resulting in a 403 or 500 status), the detail message will reflect the exception raised by the `vitap-vtop-client`.