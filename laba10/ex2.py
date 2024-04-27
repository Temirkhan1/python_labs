import csv
import psycopg2
from config import *

#function to insert data from a CSV file into the Phonebook table
def insert_data_from_csv():
    try:
        # Establishing a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        #setting autocommit to True to commit each transaction immediately
        connection.autocommit = True

        with connection.cursor() as cursor:
            
            with open("data.csv", mode='r', newline='') as file:
                # Creating a CSV reader object
                reader = csv.reader(file)
                # Skipping the header row
                next(reader)
                # Iterating through each row in the CSV file
                for row in reader:
                    # Executing SQL INSERT query to insert data into Phonebook table
                    cursor.execute("""
                        INSERT INTO Phonebook (user_name, id, phone_number)
                        VALUES (%s, %s, %s)
                    """, (row[0], row[1], row[2]))
            print("Data inserted from CSV ")

    except Exception as ex:
        print("[INFO] Error while inserting data:", ex)

    finally:
        #closing the database connection in the finally block
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")


#function to insert data from console input into the Phonebook table
def insert_data_from_console():

    user_name = input("Enter name: ")
    id = int(input("Enter id: "))
    phone_number = int(input("Enter phone number: "))
    
    try:
        #establishing a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
      
    
        connection.autocommit = True

        with connection.cursor() as cursor:
            # Executing SQL INSERT query to insert data into Phonebook table
            cursor.execute("""
                INSERT INTO Phonebook (user_name, id, phone_number)
                VALUES (%s, %s, %s)
            """, (user_name, id, phone_number))
            
        print("Data inserted from console")

    except Exception as ex:
        print("[INFO] Error while inserting data from console:", ex)

    finally:
        # Closing the database connection in the finally block
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")

# Calling the functions to insert data from CSV and console input
insert_data_from_csv() 
insert_data_from_console()
