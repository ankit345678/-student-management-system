# -student-management-system
A beginner-friendly Python web application that helps schools and teachers manage student information digitally. Built with Flask (a simple Python web framework), this system lets you:
What it does:

Add new students - Store student names, ages, grades, and email addresses
View all students - See a complete list of enrolled students
Find specific students - Look up individual student records by ID
Update information - Modify student details when needed
Remove students - Delete records when students leave

How it works:

Uses Python Flask to create a web server
Stores data temporarily in memory (resets when restarted)
Provides REST API endpoints (web URLs that accept data)
Returns information in JSON format (easy-to-read data structure)
Includes error handling for common mistakes

 Technologies Used:

Python 3.11
Flask 2.3.3 - Web framework
Requests 2.31.0 - HTTP client library

Prerequisites:

Python 3.7 or higher
pip (Python package manager)

Installation & Setup:

Install dependencies
bashpip install -r requirements.txt

Run the application
 app.py

Access the API

Server runs on: http://localhost:5000
Automatically loads 30 students from https://dummyjson.com/users



API Endpoints
1. Get All Students
httpGET /students
Response:
json{
  "success": true,
  "count": 30,
  "data": [...]
}
2. Get Student by ID
httpGET /students/1
Response:
json{
  "success": true,
  "data": {
    "id": 1,
    "firstName": "Emily",
    "lastName": "Johnson",
    "email": "emily.johnson@x.dummyjson.com",
    "phone": "+81 965-431-3024",
    "age": 28,
    "address": "626 Main Street, Phoenix"
  }
}
3. Add New Student
httpPOST /students
Content-Type: application/json
Request Body:
json{
  "firstName": "John",
  "lastName": "Doe",
  "email": "john.doe@example.com",
  "phone": "+1-555-0123",
  "age": 22,
  "address": "123 Main St, City, State"
}
Response:
json{
  "success": true,
  "message": "Student added successfully",
  "data": {...}
}
4. Dashboard Statistics
httpGET /dashboard/stats
Response:
json{
  "success": true,
  "data": {
    "totalStudents": 30,
    "averageAge": 32.6,
    "oldestStudent": 45,
    "youngestStudent": 22,
    "studentsWithPhone": 30,
    "studentsWithAddress": 30
  }
}
Testing:
Using Browser:

Visit http://localhost:5000/students
Visit http://localhost:5000/dashboard/stats
Visit http://localhost:5000/students/1

Using curl:
bash# Get all students
curl http://localhost:5000/students

# Get specific student
curl http://localhost:5000/students/1

# Add new student
curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "age": 22
  }'

# Get dashboard stats
curl http://localhost:5000/dashboard/stats
📁 Project Structure
student-management-system/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── test_post.py       # POST endpoint testing script
└── README.md          # This documentation
 Technical Implementation

Data Source: Fetches initial data from https://dummyjson.com/users
Storage: In-memory Python list (resets on server restart)
Error Handling: Comprehensive error responses with proper HTTP status codes
Data Validation: Required field validation for POST requests
Statistics: Real-time calculation of student metrics

 Assignment Requirements Met
 Backend Development: Complete REST API
 Technology: Python/Flask (as specified)
 Core Endpoints: All 4 endpoints implemented
 Data Initialization: Auto-fetch from dummyjson.com
 Storage: In-memory (no database)
Output: JSON responses

 Key Features

Automatic Data Loading: Fetches 30 real users on startup
Robust Error Handling: Proper HTTP status codes and error messages
Input Validation: Prevents duplicate emails and missing required fields
Statistics Dashboard: Real-time metrics calculation
Professional Structure: Clean, maintainable code



