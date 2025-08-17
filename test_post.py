import requests
import json

print("Testing POST /students endpoint...")

# Test data for new student
new_student = {
    "firstName": "John",
    "lastName": "Doe", 
    "email": "john.doe@test.com",
    "phone": "123-456-7890",
    "age": 25,
    "address": "123 Test Street"
}

try:
    response = requests.post('http://localhost:5000/students', json=new_student)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 201:
        print(" SUCCESS: New student added!")
    else:
        print("FAILED: Something went wrong")
        
except Exception as e:
    print(f" ERROR: {e}")