def check_grade_1(grade):
    if grade >= 90:
        print("Grade: A")
    if grade >= 80:
        print("Grade: B")
    if grade >= 70:
        print("Grade: C")
    if grade >= 60:
        print("Grade: D")
    if grade < 60:
        print("Grade: F")

def check_grade_2(grade):
    if grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    elif grade >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

grade = 85
print("This results from multiple if statements:")
check_grade_1(grade)
print()
print("This results from if, elif, else construction:")
check_grade_2(grade)
