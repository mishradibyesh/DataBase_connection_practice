"""
@author: Dibyesh Mishra
@date: 26-12-2021 23:39
"""
from getpass import getpass
from mysql.connector import connect, Error
import os
from dotenv import load_dotenv
load_dotenv()


class DBConnection:
    """Contains method which establishes connection with database"""

    @staticmethod
    def establish_connection():
        """
        Establish connection with database
        return: connection
        """
        try:
            connection=connect(
                host=os.getenv('host'),
                user=os.getenv('user_name'),
                password=os.getenv('pass'),
                database='student_details'
            )
            print("Connection established successfully...")
            return connection
        except Error as e:
            print(e)


class DatabaseOperations:
    def __init__(self):
        self.connection = DBConnection.establish_connection()
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        """
        desc: execute query by passing it to cursor method
        param : query:
        return:None
        """
        self.cursor.execute(query)
        self.connection.commit()


    def show_databases(self):
        """Shows all the databases"""
        self.cursor.execute('show databases')
        for database in self.cursor.fetchall():
            print(database)

    def show_tables(self):
        self.cursor.execute('show tables')
        for database in self.cursor.fetchall():
            print(database)

    def insert_in_table(self):
        """
        query to insert into table
        """
        query = "INSERT INTO pet VALUES ('german','sheffered','trester','M','1999-03-30',NULL);"
        query1 = "INSERT INTO pet VALUES ('pitBull','ramesh','trester','M','1999-03-30',NULL);"
        self.execute_query(query1)
        self.execute_query(query)
        print("inserted successfully")

    def show_table_data(self):
        query = "select * from pet"
        self.execute_query(query)

    def describe_table(self):
        self.cursor.execute('describe pet')
        for database in self.cursor.fetchall():
            print(database)

    def show_data(self, query):
        """
        Shows all the data for the query passed
        param : query
        return: None
        """
        self.cursor.execute(query)
        for data in self.cursor.fetchall():
            print(data)

    def create_table(self):
        "query to create table "

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
        self.execute_query(query)
        self.execute_query(query2)


operation = DatabaseOperations()
operation.describe_table()
operation.show_databases()
operation.show_tables()
operation.insert_in_table()
operation.execute_query("UPDATE pet SET owner='Dibyesh' WHERE name='german'")
operation.show_data('SELECT * FROM pet')
operation.execute_query("DELETE FROM pet WHERE name = 'ramesh'")