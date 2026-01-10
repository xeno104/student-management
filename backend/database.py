import mysql.connector


try: 
    mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="student_management"
    )
    mycursor = mydb.cursor()
except mysql.connector.Error as err: 
    print(f"Database connection failed {err}")
else:
    print("Database connected successfully")
    


    


mycursor.execute("SELECT * FROM user;")

tables = mycursor.fetchall()
print(tables)

