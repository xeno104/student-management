
from backend.database import check_database_exist, create_table
from frontend.loginScreen import loginScreen
from frontend.register_screen import registerScreen

logged_in = 0

def main():
    
    db_check_result = check_database_exist()
    
    if(db_check_result):
        if(logged_in == 0):
            loginScreen()
    
    else:
        
        create = create_table("auth-table.csv")
        if(not create):
            print("Something went wrong!")
            main()
            
        register = registerScreen()
        
        if register:
            registerScreen
        else:
            pass
            
        
        
        
        
    
            
       

main()




# auth_table.csv

# uid(int-unique), name(string), username(string), password(string)














#student_db.csv

# uid(int unique), first_name(string), last_name(string), address(string), mobile_no(int or string), class(string or int), roll_no(int - unique), subject_name (string), subject_marks (string)

