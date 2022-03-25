import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="gorilla", user='postgres', password='root', host='localhost', port= '5432'
)
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO EMPLOYEE(userid, name, email, password) VALUES (111, 'Ramya', 'rama@d.com', 3327)''')

# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()