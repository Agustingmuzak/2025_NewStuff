class Student:
    def __init__(self, first, last, student_number):
        self.first = first
        self.last = last
        self.student_number = student_number
    def studentprint(self):
        return '{} {} {}'.format(self.first, self.last, self.student_number)


student_1 = Student('Agustin', 'Gonzalez', 3)

print(student_1.studentprint())