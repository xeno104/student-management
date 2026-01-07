def registerScreen():
    
    print("\n\n Register your admin account\n\n")
    
    name = str(input("Enter your name: "))
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    
    if(name == "" and username == "" and password == ""):
        print("Fill all fields.")
        return 0
    
    return [name, username, password]