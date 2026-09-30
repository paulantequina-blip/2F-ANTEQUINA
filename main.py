from student import Student
from name import get_name
from grades import get_grades
from average import get_average
from display import get_print


def main():
    name = get_name()
    grades = get_grades()
    average = get_average(grades)
    get_print(name, average)


main()

name = input("Enter Name: ")

grades = {}

while True:
    try:
        print()
        prelim = float(input("Enter Prelim Grade: "))
        midterm = float(input("Enter Midterm Grade: "))
        prefinal = float(input("Enter Prefinal Grade: "))
        final = float(input("Enter Final Grade: "))

        if prelim or midterm or prefinal or final is not None:
            grades['prelim'] = prelim
            grades['midterm'] = midterm
            grades['prefinal'] = prefinal
            grades['final'] = final
            break
    except ValueError:
        print("Incorrect Input. Please enter a proper grade.")

student1 = Student(name, grades)
student1.display()