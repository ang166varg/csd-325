import json

# Load the JSON file into a class list
with open("student.json.py", "r") as file:
    student_list = json.load(file)

# Function to print student data
def print_students(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Notify and print the original list
print("Original Student List:")
print_students(student_list)

# Append your own student record
new_student = {
    "F_Name": "Angela",
    "L_Name": "Vargas",
    "Student_ID": 99999,
    "Email": "avargas@example.com"
}
student_list.append(new_student)

# Notify and print the updated list
print("\nUpdated Student List:")
print_students(student_list)

# Save the updated list back to the JSON file
with open("student.json", "w") as file:
    json.dump(student_list, file, indent=4)

# Final confirmation message
print("\nThe student.json file has been updated.")