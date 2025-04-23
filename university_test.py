import requests

# This api add/creates a new student in the system
## json is the data we send as json in the body of the request
## headers contains information for the server needed to execute the request. In this case, we specify that we are sending content in the form of json.
add_student_response = requests.post("http://127.0.0.1:5000/students",
                                     json={'name': 'Test Student', 'contact_info': {'email': 'test_student@gmail.com', 'phone': '+49-555-3030'}},
                                     headers={'Content-Type': 'application/json'})
print(f"Response of POST to '/students': {add_student_response.json()}")

get_students_response = requests.get("http://127.0.0.1:5000/students")
print(f"Response of GET to '/students': {list(get_students_response.json()['students'])}")

# print(list(get_students_response.json()['students']))
print(len(list(get_students_response.json()['students'])))

