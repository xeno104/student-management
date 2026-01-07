def check_database_exist():
    try:
        y = open("./database/auth_table.csv", 'r')
        return 1
    except: 
        return 0

def create_table(name):
    if type(name) == str:
        
        file_name = "./database/"+name
        try:
            
            file = open(file_name, 'x')
            if(file):
                return 1
        except:
            return 0
    else:
        return 0
        
    