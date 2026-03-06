def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid login")

login()

# This line is modified on the conflict-branch
print("Conflict Branch: Security Update v2")