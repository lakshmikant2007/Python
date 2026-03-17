import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()

# Create Database
cursor.execute("CREATE DATABASE SELECTION_DB")

print("Database created successfully")

# Close connection
conn.close()