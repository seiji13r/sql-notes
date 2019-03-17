from dotenv import load_dotenv
import psycopg2 as pg2
import os

# Load Environmental Variables From .env
# Make sure the file .env exist with the right connection values
load_dotenv()

# Define the Connection Values
DBHOST = os.getenv("POSTGRESQL_HOST")
DBPORT = os.getenv("POSTGRESQL_PORT")
DB = os.getenv("POSTGRESQL_DB")
DBUSER = os.getenv("POSTGRESQL_USER")
DBPASSWORD = os.getenv("POSTGRESQL_PASSWORD")

# Create the Connection using the previous Connection Values
conn = pg2.connect(
    host=DBHOST, port=DBPORT, database=DB, user=DBUSER, password=DBPASSWORD)

# Create Cursor
cursor = conn.cursor()

# Execute the SQL query using the cursor
cursor.execute('SELECT * FROM payment;')

# Retrieve a List of 10 records from the Query
data = cursor.fetchmany(100)
print(data)

print('\n\n')

# Retrieve a List of 10 records from the Query
# data = cursor.fetchall()
# print(data)