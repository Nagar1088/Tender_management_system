import mysql.connector

# Function to establish a connection to the database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="S@16112001",
        database="tender_management_system"
    )
