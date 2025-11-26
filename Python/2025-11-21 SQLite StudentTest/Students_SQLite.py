import sqlite3
from Students import Student

conn = sqlite3.connect('school.db')

c = conn.cursor()

# c.execute("""CREATE TABLE student (
#           first_name text, 
#           last_name text,
#           email_address text,
#           student_number int UNIQUE PRIMARY KEY
#           )""")

# c.execute("ALTER TABLE student ADD COLUMN student_number INTEGER")


# students_data = c.execute("SELECT * FROM student")
# print(students_data.description)


def insert_student(first: str, last: str, email:str, studentnumber: int):
    c.execute("INSERT INTO student VALUES (:first, :last, :email, :studentnumber)", {
        'first':first,
        'last':last,
        'email':email,
        'studentnumber':studentnumber
    })

def get_studentdetail(studentnumber: int):
    c.execute("SELECT * FROM student WHERE student_number=:studentnumber", {'studentnumber': studentnumber})
    return c.fetchall()

