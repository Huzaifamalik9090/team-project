def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid login")

login()
print("Main and Conflict branch merged")