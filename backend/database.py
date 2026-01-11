import mysql.connector


def connect_database():
    try: 
        mydb = mysql.connector.connect(
        host="database-2.cjg8o8cmckqi.ap-south-1.rds.amazonaws.com",
        port=3306,
        user="admin",
        password="$*5H3_Xs4#PN>~",
        database="database2"
        )
        mycursor = mydb.cursor()
        
        
    except mysql.connector.Error as err: 
        print(f"Database connection failed {err}")
    else:
        print("Database connected successfully")

connect_database()

def login(username, password):
    
    pass
    
