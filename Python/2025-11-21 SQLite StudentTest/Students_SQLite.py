import sqlite3
from Students import Student

conn = sqlite3.connect('school.db')

c = conn.cursor()

# c.execute("""CREATE TABLE students (
#           first_name text, 
#           last_name text,
#           email_address text,
#           )""")

# c.execute("ALTER TABLE students ADD COLUMN student_number INTEGER")


# students_data = c.execute("SELECT * FROM students")
# print(students_data.description)


def insert_student(first: str, last: str, email:str, studentnumber: int):
    c.execute("INSERT INTO students VALUES (:first, :last, :email, :studentnumber)", {
        'first':first,
        'last':last,
        'email':email,
        'studentnumber':studentnumber
    })

def get_studentdetail(studentnumber: int):
    c.execute("SELECT * FROM students WHERE student_number=:studentnumber", {'studentnumber': studentnumber})
    return c.fetchall()

student1 = Student('Agustin', 'Gonzalez')

""" insert_student(student1.first_name,
               student1.last_name,
               student1.email,
               student1.student_number) """

get_studentdetail(1)