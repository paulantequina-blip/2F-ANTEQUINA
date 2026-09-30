def get_grades():
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
                return grades
        except ValueError:
            print("Incorrect Input. Please enter a proper grade.")