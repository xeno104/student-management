def check_login(username, password):
    pass


def check_database_exist():
    
    try:
        y = open("../database/login.txt", 'r')
        if(y):
            print("File Found")
    except FileNotFoundError: 
        print("File Not Found")
    