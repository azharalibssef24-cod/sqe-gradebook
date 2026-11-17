# Lab 12 – API Manual Exploration

## Objective
To manually test the GradeBook REST API using PowerShell and verify successful and unsuccessful HTTP requests.

**Base URL:** `http://127.0.0.1:5000`

## 1. Create Student

- **Method:** POST
- **Endpoint:** `/students`
- **Request Body:**
```json
{
  "name": "Ali",
  "roll_no": 101
}
```
- **Status Code:** 201 Created
- **Response:**
```json
{
  "name": "Ali",
  "roll_no": 101,
  "average": 0.0
}
```
- **Result:** Passed

## 2. Get Student Details

- **Method:** GET
- **Endpoint:** `/students/101`
- **Status Code:** 200 OK
- **Response:**
```json
{
  "name": "Ali",
  "roll_no": 101,
  "average": 0.0
}
```
- **Result:** Passed

## 3. Add Student Score

- **Method:** POST
- **Endpoint:** `/students/101/scores`
- **Request Body:**
```json
{
  "score": 80
}
```
- **Status Code:** 200 OK
- **Response:**
```json
{
  "message": "Score added successfully",
  "roll_no": 101,
  "score": 80
}
```
- **Result:** Passed

## 4. Get Student Average

- **Method:** GET
- **Endpoint:** `/students/101/average`
- **Status Code:** 200 OK
- **Response:**
```json
{
  "roll_no": 101,
  "average": 80.0
}
```
- **Result:** Passed

## 5. Get All Students

- **Method:** GET
- **Endpoint:** `/students`
- **Status Code:** 200 OK
- **Response:**
```json
[
  {
    "name": "Ali",
    "roll_no": 101,
    "average": 80.0
  }
]
```
- **Result:** Passed

## 6. Invalid Request – Missing Name

- **Method:** POST
- **Endpoint:** `/students`
- **Request Body:**
```json
{
  "roll_no": 102
}
```
- **Status Code:** 400 Bad Request
- **Response:**
```json
{
  "error": "Both name and roll_no are required"
}
```
- **Result:** Passed – API correctly rejected the missing name.

## 7. Invalid Request – Incorrect Name Type

- **Method:** POST
- **Endpoint:** `/students`
- **Request Body:**
```json
{
  "name": 123,
  "roll_no": 102
}
```
- **Status Code:** 400 Bad Request
- **Response:**
```json
{
  "error": "Name must be a string"
}
```
- **Result:** Passed – API correctly rejected the numeric name.

## Conclusion

All five required API endpoints were manually tested successfully. Two invalid requests were also tested and correctly rejected with HTTP 400 responses. The API returned the expected JSON data and status codes.