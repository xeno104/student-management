def check_database_exist(name):
    
    if(not type(name) == str):
        raise "name should be string"
    try:
        y = open("./database/"+name, 'r')
        return 1
    except: 
        return 0

def create_table(name):
    if type(name) == str:
        
        file_name = "./database/"+name
        try:
            
            file = open(file_name, 'w')
            file.write('uid, name, username, password')
            if(file):
                return 1
        except:
            return 0
    else:
        return 0
        
    