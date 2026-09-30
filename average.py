def get_average(grades):
    total = 0

    for grade in grades.values():
        total += grade

    return total / 4