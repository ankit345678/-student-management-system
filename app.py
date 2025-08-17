# Import the tools we need
from flask import Flask, jsonify, request
import requests
from datetime import datetime

# Create our Flask application
app = Flask(__name__)

# This is our in-memory storage for students 
students = []

print("Student Management System starting...")


def fetch_initial_data():
    """Get student data from dummyjson.com when app starts"""
    try:
        print("Fetching student data from DummyJSON...")
        response = requests.get('https://dummyjson.com/users')
        
        if response.status_code == 200:
            users = response.json()['users']
            global students
            students = []
            
            # Convert each user to our student format
            for user in users:
                student = {
                    'id': user['id'],
                    'firstName': user['firstName'], 
                    'lastName': user['lastName'],
                    'email': user['email'],
                    'phone': user['phone'],
                    'age': user['age'],
                    'address': f"{user['address']['address']}, {user['address']['city']}"
                }
                students.append(student)
            
            print(f"✅ Successfully loaded {len(students)} students!")
            return True
        else:
            print(" Failed to fetch data")
            return False
            
    except Exception as e:
        print(f" Error: {e}")
        return False
@app.route('/students', methods=['GET'])
def get_all_students():
    """When someone visits /students, show all students"""
    return jsonify({
        'success': True,
        'count': len(students),
        'data': students
    })
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    """When someone visits /students/1, show student with ID 1"""
    for student in students:
        if student['id'] == student_id:
            return jsonify({
                'success': True,
                'data': student
            })
    
    return jsonify({
        'success': False,
        'error': 'Student not found'
    }), 404
@app.route('/students', methods=['POST'])
def add_student():
    """When someone sends POST to /students, add a new student"""
    try:
        data = request.get_json()
        
        # Check if required fields are provided
        required_fields = ['firstName', 'lastName', 'email']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }), 400
        
        # Check if email already exists
        for student in students:
            if student['email'] == data['email']:
                return jsonify({
                    'success': False,
                    'error': 'Student with this email already exists'
                }), 400
        
        # Create new student
        new_student = {
            'id': len(students) + 1,  # Simple ID generation
            'firstName': data['firstName'],
            'lastName': data['lastName'],
            'email': data['email'],
            'phone': data.get('phone', ''),
            'age': data.get('age', 0),
            'address': data.get('address', '')
        }
        
        students.append(new_student)
        
        return jsonify({
            'success': True,
            'message': 'Student added successfully',
            'data': new_student
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error adding student: {str(e)}'
        }), 500
@app.route('/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    """Provide basic statistical data"""
    if not students:
        return jsonify({
            'success': True,
            'data': {
                'totalStudents': 0,
                'averageAge': 0,
                'oldestStudent': 0,
                'youngestStudent': 0
            }
        })
    
    # Calculate statistics
    total_students = len(students)
    ages = [s['age'] for s in students if s['age'] > 0]
    average_age = sum(ages) / len(ages) if ages else 0
    oldest_age = max(ages) if ages else 0
    youngest_age = min(ages) if ages else 0
    
    return jsonify({
        'success': True,
        'data': {
            'totalStudents': total_students,
            'averageAge': round(average_age, 1),
            'oldestStudent': oldest_age,
            'youngestStudent': youngest_age,
            'studentsWithPhone': len([s for s in students if s['phone']]),
            'studentsWithAddress': len([s for s in students if s['address']])
        }
    })
if __name__ == '__main__':
    print("Starting Student Management System...")
    
    # Get initial data from internet
    if fetch_initial_data():
        print("Data loaded!")
    else:
        print("Starting with empty data!!")
    
    print(" Server starting on http://localhost:5000")
    app.run(debug=True, port=5000)    