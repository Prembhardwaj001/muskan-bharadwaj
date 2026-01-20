# Step 1: Create a dictionary of student marks
student_marks = {
    "Prem": 85,
    "Rahul": 78,
    "Anjali": 92,
    "Sneha": 88
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show message
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Student not found.")
