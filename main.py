import app_access

print("""Welcome to my Task manager app.
      - Made by Adhyan Chandhoke
      """)

while (True):
    user_choice = input("Would you like to Login or Signin: ").lower()  
        
    if user_choice == "login":
        app_access.login()
    if user_choice == "signin":
        app_access.signin()
    else:
        print("Invalid input. Please choose either one: login or signin")
        
    