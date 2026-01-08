
from backend.database import check_database_exist, create_table
from frontend.loginScreen import loginScreen
from frontend.register_screen import registerScreen
import pandas as pd

logged_in = 0

def register(auth_table_name):
    create = create_table(auth_table_name)
    if(not create):
        print("Auth Table Creation Error!!")
        return 0
            
    register = registerScreen()
 
        
    if register:
        try: 
            auth_table = open('./database/'+auth_table_name, 'a')
            auth_table.write(f'\n0,{register[0]},{register[1]},{register[2]}')
        except:
            print("Error While Registering!!!")
        else:
            print("Resgistered Successful.. :)")
            loginScreen()
                
    else:
        print("Error while Registering Admin!!")
        return 0



def main():
    
    auth_table_name = 'auth-table.csv'
    credentials = False
    db_check_result = check_database_exist(auth_table_name)
    
    if(db_check_result):
        credentials = pd.read_csv('./database/'+auth_table_name, nrows=1)
    
    if(db_check_result and not credentials.empty):

        if(logged_in == 0):
            loginScreen()
            
    else:
        register(auth_table_name)
        
        
            
        
        
        
        
    
            
       

main()




# auth_table.csv

# uid(int-unique), name(string), username(string), password(string)














#student_db.csv

# uid(int unique), first_name(string), last_name(string), address(string), mobile_no(int or string), class(string or int), roll_no(int - unique), subject_name (string), subject_marks (string)

