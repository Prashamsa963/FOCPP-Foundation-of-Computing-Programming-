# Lab group calculator

students = int(input("How many students? "))
group_size = int(input("Required group size? "))

groups = students // group_size
leftover = students % group_size

# Fix grammar for "student/students"
if leftover == 1:
    student_word = "student"
else:
    student_word = "students"

print(f"There will be {groups} groups with {leftover} {student_word} left over.")
