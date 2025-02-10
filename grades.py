grade = int(input ("Grade: "))

if grade <= 100 and grade >= 90:
    grade = "A"
elif grade <= 89 and grade >= 80:
    grade = "B"
elif grade <= 79 and grade >= 70:
    grade = "C"
elif grade <= 69 and grade >= 60:
    grade = "D"
elif grade <= 59:
    grade = "F"

print (f" Your grade is a(n) {grade}")