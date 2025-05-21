# VIT-AP VTOP API Documentation

Welcome to the detailed documentation for the VIT-AP VTOP API. This document provides information about all available endpoints, request parameters, and response formats.

## Table of Contents
1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [General Endpoints](#general-endpoints)
4. [Data Retrieval Endpoints (Login Required)](#data-retrieval-endpoints-login-required)
5. [Outing Management Endpoints (Login Required)](#outing-management-endpoints-login-required)
6. [Error Handling](#error-handling)

## Introduction
The VIT-AP VTOP API allows students to programmatically access their academic information from the VIT-AP VTOP Portal. All login-required endpoints first authenticate the user with the VTOP system using the provided credentials and then fetch the requested data.

## Authentication
All requests to this API must include an `API-KEY` in the request headers.
```
API-KEY: YOUR_API_KEY
```
Requests without a valid API key will result in a `401 Unauthorized` error.

For endpoints under the `/login/` path, user credentials (`username` and `password`) are required in the request body to authenticate with the VTOP portal.

## General Endpoints

### 1. Welcome Message
- **GET /**
  - **Description**: Returns a default welcome message.
  - **Response**:
    ```text
    You can access this API on Github
    ```

### 2. Hello World
- **GET /helloworld**
  - **Description**: A simple test endpoint that returns "Hello World".
  - **Response**:
    ```text
    Hello World
    ```

### 3. Get Captcha
- **GET /getcaptcha**
  - **Description**: Fetches a captcha image and a CSRF token required for the login process. The captcha image is returned directly, and the CSRF token is managed server-side within the session.
  - **Response**: Captcha image (e.g., `image/png`).

## Data Retrieval Endpoints (Login Required)
These endpoints require `username` and `password` in the JSON request body for VTOP authentication.

### 1. Get All Data
- **POST /login/getalldata**
  - **Description**: Logs in and retrieves a comprehensive set of data including profile, attendance, timetable, exam schedule, and marks.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "semSubID": "your_semester_ID"
    }
    ```
  - **Response**:
    ```json
    {
      "profile": { /* user profile details */ },
      "attendance": { /* attendance details */ },
      "timetable": { /* timetable details */ },
      "exam_schedule": { /* exam schedule details */ },
      "marks": { /* marks details */ }
    }
    ```

### 2. Get User Profile
- **POST /login/profile**
  - **Description**: Logs in and retrieves the user's profile information.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - **Response**:
    ```json
    {
      "profile": { /* user profile details */ }
    }
    ```

### 3. Get Timetable
- **POST /login/timetable**
  - **Description**: Logs in and retrieves the user's class timetable for a specific semester.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "semSubID": "your_semester_ID"
    }
    ```
  - **Response**:
    ```json
    {
      "timetable": { /* timetable details */ }
    }
    ```

### 4. Get Attendance
- **POST /login/attendance**
  - **Description**: Logs in and retrieves the user's attendance details for a specific semester.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "semSubID": "your_semester_ID"
    }
    ```
  - **Response**:
    ```json
    {
      "attendance": { /* attendance details */ }
    }
    ```

### 5. Get Marks
- **POST /login/marks**
  - **Description**: Logs in and retrieves the user's marks for a specific semester.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "semSubID": "your_semester_ID"
    }
    ```
  - **Response**:
    ```json
    {
      "marks": { /* marks details */ }
    }
    ```

### 6. Get Exam Schedule
- **POST /login/examschedule**
  - **Description**: Logs in and retrieves the user's exam schedule for a specific semester.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "semSubID": "your_semester_ID"
    }
    ```
  - **Response**:
    ```json
    {
      "exam_schedule": { /* exam schedule details */ }
    }
    ```

### 7. Get Biometric Log
- **POST /login/biometric**
  - **Description**: Logs in and retrieves the user's biometric (in/out) logs for a specific date.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "date": "YYYY-MM-DD"
    }
    ```
  - **Response**:
    ```json
    {
      "biometric_log": { /* biometric log details */ }
    }
    ```

### 8. Get Payments
- **POST /login/payments**
  - **Description**: Logs in and retrieves payment details associated with the user's application number.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "applno": "your_application_number"
    }
    ```
  - **Response**:
    ```json
    {
      "payments": { /* payment details */ }
    }
    ```

### 9. Get Payment Receipts
- **POST /login/paymentsreceipts**
  - **Description**: Logs in and retrieves a list of payment receipts for the user.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "applno": "your_application_number"
    }
    ```
  - **Response**:
    ```json
    {
      "payment_receipts": [ /* list of payment receipts */ ]
    }
    ```

### 10. Print Payment Receipt
- **POST /login/printpaymentreceipt**
  - **Description**: Logs in and retrieves data for a specific payment receipt.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "applno": "your_application_number",
      "receitNo": "receipt_number"
    }
    ```
  - **Response**:
    ```json
    {
      "payment_receipts": { /* specific payment receipt details */ }
    }
    ```

### 11. Get NCGPA Rank Details
- **POST /login/ncgparankdetails**
  - **Description**: Logs in and retrieves NCGPA rank details for the user.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - **Response**:
    ```json
    {
      "ncgpa_rank_details": { /* NCGPA rank details */ }
    }
    ```

## Outing Management Endpoints (Login Required)
These endpoints require `username` and `password` in the JSON request body for VTOP authentication.

### 1. Submit Weekend Outing Form
- **POST /login/weekendoutingform**
  - **Description**: Logs in and submits a weekend outing request form.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "outPlace": "Place of Visit",
      "purposeOfVisit": "Purpose of Visit",
      "outingDate": "YYYY-MM-DD",
      "outTime": "HH:MM AM/PM",
      "contactNumber": "Your Contact Number"
    }
    ```
  - **Response**:
    ```json
    {
      "weekend_outing": "Status message from VTOP (e.g., 'Successfully submitted')"
    }
    ```

### 2. Submit General Outing Form
- **POST /login/generaloutingform**
  - **Description**: Logs in and submits a general outing request form.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password",
      "outPlace": "Place of Visit",
      "purposeOfVisit": "Purpose of Visit",
      "outingDate": "YYYY-MM-DD",
      "outTime": "HH:MM AM/PM",
      "inDate": "YYYY-MM-DD",
      "inTime": "HH:MM AM/PM"
    }
    ```
  - **Response**:
    ```json
    {
      "general_outing": "Status message from VTOP (e.g., 'Successfully submitted')"
    }
    ```

### 3. Get General Outing Requests
- **POST /login/generaloutingrequests**
  - **Description**: Logs in and retrieves the status of submitted general outing requests.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - **Response**:
    ```json
    {
      "booking_requests": { /* details of general outing requests */ }
    }
    ```

### 4. Get Weekend Outing Requests
- **POST /login/weekendoutingrequests**
  - **Description**: Logs in and retrieves the status of submitted weekend outing requests.
  - **Request Body**:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
  - **Response**:
    ```json
    {
      "booking_requests": { /* details of weekend outing requests */ }
    }
    ```

## Error Handling
The API returns appropriate HTTP status codes and error messages for invalid requests or server-side issues. Common errors include:
- `400 Bad Request`: Invalid request format or missing parameters.
- `401 Unauthorized`: Authentication failed (Invalid API Key or VTOP credentials).
- `403 Forbidden`: Access denied.
- `404 Not Found`: Resource not found.
- `500 Internal Server Error`: An error occurred on the server.