# importing sqlite3 into the py file
import sqlite3
from Employee import Employee

#conn is a variable name which establishes the connection to the db
# employee.db is created in Python\employee.db
#if we wanted to create an in memory database instead we could use sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')

#creating a cursor allows us to start executing SQL commands
# variable name can be anything
c = conn.cursor()

#execute runs SQL commands, triple quotes are so we can run commands that
#span multiple lines

# c.execute("""CREATE TABLE employees (
#           first text, 
#           last text,
#           pay integer
#           )""")

emp_1 = Employee('Olga', 'Amaro', 80000)
emp_2 = Employee('Facundo', 'Toledo', 77000)

# print(emp_1.first) 

# c.execute("INSERT INTO employees VALUES ('Jose', 'Gonzalez', 50)")


#This is one way on inserting employee values into the database using ? placeholders, 
#The INSERT statemente is passed as a first argument to the execute function
#The (emp_1.first, emp_1.last, emp_1.pay) tuple is passed as a second argument...
#To the execute function

# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

#This is another way of inserting employee object values into the database using :value placeholders
#The INSERT statement is passed as a first argument to the execute function
#A dictionary is passed as a second argument to the execute function

# c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {
#     'first':emp_2.first,
#     'last':emp_2.last,
#     'pay':emp_2.pay
#     })

#This is one way of selecting values from the database by directly entering the value to fetch

#The function below inserts an employee object into the DB by passing emp.first, etc values
#The with.conn statement is a context manager, it will automatically commit our transaction
#The transaction will be committed automatically unless there's an exception

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees values (:first, :last, :pay)", {
            'first':emp.first, 
            'last':emp.last,
            'pay':emp.pay
        })

def get_emps_by_name(lastname):
        c.execute("SElECT * FROM employees WHERE last=:last", {'last': lastname})
        return c.fetchall()

def update_pay(emp, pay):
     with conn:
          c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""", 
                    {'first': emp.first, 'last':emp.last, 'pay':emp.pay})
          
def remove_emp(emp):
     with conn:
          c.execute("DELETE from employees WHERE first =:first AND last =:last", {
               'first': emp.first, 
               'last':emp.last
          })

# c.execute("SELECT * FROM employees WHERE last='Gonzalez'")

#This is one way of selecting values using a placeholder
#When using the ? placeholder if our tuple only has one value we will need to insert...
#a coma after the value to turn it into a tuple

# c.execute("SELECT * FROM employees WHERE last=?", ('Amaro',))


#This is another way of selecting values using a dictionary placeholder
# c.execute("SELECT * FROM employees WHERE last=:last", {'last':emp_2.last})
emp_3 = Employee('Micaela', 'Cerqueira', 90000)

conn.commit()

#conn.close() closes out our connection to the DB
conn.close()