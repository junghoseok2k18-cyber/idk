import re

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
student_id = input("Enter student ID number: ")

first_initial = first_name[0].lower()
last_name = last_name.lower()

email = f"{first_initial}.{last_name}.{student_id}@umindanao.edu.ph"

pattern = r"^[a-z]\.[a-z]+\.\d+@umindanao\.edu\.ph$"

if re.match(pattern, email):
    status = "valid"
else:
    status = "invalid"

print()
print("Generated email:", email)
print("The email is", status)
