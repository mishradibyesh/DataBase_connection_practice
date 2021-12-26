"""
@author: Dibyesh Mishra
@date: 26-12-2021 23:39
"""
from getpass import getpass
from mysql.connector import connect, Error

def connection(query):
    try:
        with connect(host="localhost",
                     user="root",
                     password="Dibyesh@3",
                     database="student_details")as connection:
                    print(connection)
                    with connection.cursor() as cursor:
                        cursor.execute(query)
                        for values in cursor.fetchall():
                            print(values)
    except Error as e:
        print(e)

def create_table():
    query = "CREATE TABLE Persons " \
            "(PersonID int," \
            "LastName varchar(255)," \
            "FirstName varchar(255)," \
            "City varchar(255));"
    query2 = "CREATE TABLE pet(name VARCHAR(20)," \
             "owner VARCHAR(20)," \
             "species VARCHAR(20)," \
             "sex CHAR(1)," \
             "birth DATE," \
             "death DATE);"
    # connection(query)
    connection(query2)

def show_tables():
    query = "show tables"
    connection(query)

show_tables()

def insert_in_table():
    query = "INSERT INTO pet VALUES ('german','sheffered','trester','M','1999-03-30',NULL);"
    query1 = "INSERT INTO pet VALUES ('pitBull','fered','trester','M','1999-03-30',NULL);"
    connection(query1)

def show_table_data():
    query = "select * from Persons"
    connection(query)

show_table_data()

def describe_table():
    query = "describe pet"
    connection(query)

describe_table()