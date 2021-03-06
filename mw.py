import subprocess as sp
import pymysql
import pymysql.cursors
from aditya import *
from suyash import *
from tushar import *
from aditya_q import *
from suyash_q import *
from tushar_q import *

def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def hireAnEmployee():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new employee's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Minit"] = name[1]
        row["Lname"] = name[2]
        row["Ssn"] = input("SSN: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Address"] = input("Address: ")
        row["Sex"] = input("Sex: ")
        row["Salary"] = float(input("Salary: "))
        row["Dno"] = int(input("Dno: "))

        query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
            row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def dispatch(ch, con, cur):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        query_1(con,cur)
    elif(ch == 2):
        query_2(con,cur)
    elif(ch == 3):
        query_3(con, cur)
    elif(ch == 4):
        query_4(con,cur)
    elif(ch == 6):
        query_6(con,cur)
    elif(ch==15):
        query_15(con, cur)
    elif(ch==16):
        query_16(con, cur)
    suy(ch, con, cur)
    tushar(ch, con, cur)


# Global
while(1):

    # Can be skipped if you want to hard core username and password
    #tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")
    port = int(input("Port: "))
    # Set db name accordingly which have been create by you
    # Set host to the server's address if you don't want to use local SQL server
    con = pymysql.connect(host='localhost',
      user=username,
      password=password,
      db='futsal',
      port=port,
      cursorclass=pymysql.cursors.DictCursor)
    #tmp = sp.call('clear', shell=True)

    if(con.open):
        print("Connected")
    else:
        print("Failed to connect")

    tmp = input("Enter any key to CONTINUE>")

    with con.cursor() as cur:
        while(1):
        #tmp = sp.call('clear', shell=True)
        # Here taking example of Employee Mini-world
            print("1. Option 1") # Hire an Employee
            print("2. Option 2") # Fire an Employee
            print("3. Option 3") # Promote Employee
            print("4. Option 4") # Employee Statistics
            print("5. Logout")
            ch = int(input("Enter choice> "))
            #tmp = sp.call('clear', shell=True)
            dispatch(ch, con, cur)
