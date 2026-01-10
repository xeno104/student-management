import mysql.connector


try: 
    mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="student_management"
    )
except mysql.connector.Error as err: 
    print(f"Database connection failed {err}")


print("Database connected successfully")
    
mycursor = mydb.cursor()
    
mycursor.execute("SHOW TABLES")

tables = mycursor.fetchall()
print(tables)

