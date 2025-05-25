import json
import os
import features

file_path = "user_data.json"

def signin():
    print("Welcome to our signin page")
    user_mail = input("Signin-Email: ")
    user_pass = input("Signin-Pass: ")
    pass_length = len(user_pass)
    
    if '@' in user_mail and '.' in user_mail and user_mail.endswith(".com"): 
        pass
    else:
        print("Please provide the correct email")
        return
    
    if user_mail.startswith("@") or user_mail.endswith("@"):
        print("Invalid email")
        return

    if pass_length < 8:
        print("Please make sure that the password has more than 8 character") 
        return
    else:
        user_data = {
            "email" : user_mail,
            "password" : user_pass,
        }
        
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f) # creates a file with an empty list if it doesnt exist
       
        try:
            with open(file_path, 'r') as f:
                data = json.load(f) # reads/open the file to be used
        except(FileNotFoundError):
            data = []
        
        data.append(user_data)
        
        with open(file_path,'w') as f:
            json.dump(data,f, indent=4)
            
        print("Thank you for signing in, You can now go to the login page - Adhyan :D")
        return
            
def login():
    print("Welcome to our login page")
    user_mail = input("Login-Email: ")
    user_pass = input("Login-Pass: ")
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([], f)
            
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    user_found = False
    for user in data:
        if user_mail == user["email"] and user_pass == user["password"]:
            print("successfully logged in \n loading you to the home page.....")
            user_found = True
            features.home() # takes to a different file as a home page with features
            return
            
    if not user_found:
        print("Invalid credentials")
        return        

         
    
    
    