student_name = input("Student name: ")
subjects = []
grades = []
for i in range(1, 6):
    subject = input(f"Enter subject {i}: ")
    grade = int(input(f"Enter grade {i}: "))
    subjects.append(subject)
    grades.append(grade)
average = sum(grades) / len(grades)
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print("\nREPORT CARD")
print(f"Student: {student_name}")
for i in range(len(subjects)):
    print(f"{subjects[i]} grade is {grades[i]}")
print(f"Average grade: {average}")
print(f"Letter grade: {letter_grade}")
#collects the info needed, and then does the calculations