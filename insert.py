import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="gorilla", user='postgres', password='root', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
a=int(input('enter user id '))
b=input('enter name ')
c=input('enter email ')
d=input('enter password ')
sq="insert into employee values('%d','%s','%s','%s')"%(a,b,c,d)
cursor.execute(sq)
print('data saved')

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()