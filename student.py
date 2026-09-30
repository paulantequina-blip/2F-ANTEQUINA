class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def get_average(self):
        total = 0
        for grade in self.grades.values():
            total += grade
        return total / 4

    def display(self):
        average = self.get_average()
        print(f"\nHello {self.name}! Your average grade is {round(average):.0f}\n")