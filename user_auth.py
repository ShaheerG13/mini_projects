import bcrypt
import getpass
import json

try:
    with open ("user_auth.json", "r") as f:
            user_data = json.load(f)
except FileNotFoundError:
     user_data = {}


def login_check():
    # getpass prevents characters being seen while typing
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    # converts password to bytes format
    pass_bytes = password.encode('utf-8')

    # searches for username and password in database
    if username in user_data:
        stored_pass = user_data[username].encode('utf-8')
    else:
        return False

    # checks if password is correct
    return bcrypt.checkpw(pass_bytes, stored_pass)


def create_login():
    username = input("Create username: ")
    if username in user_data:
        return False
    
    while True:
        password = getpass.getpass("Create password: ")
        
        if len(password) < 8:
            print("Password must be at least 8 characters")
            continue
        
        if not any(char.isdigit() for char in password):
            print("Password must contain at least one digit")
            continue
        
        if password.lower() == password:
            print("Password must contain at least one uppercase charactrer")
            continue

        confirm = getpass.getpass("Confirm password: ")
        if password != confirm:
            print("Passwords do not match")
            continue
        break

    # hashes password with salt
    pass_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(pass_bytes, bcrypt.gensalt())
    
    # stores newly creared username and password in json file
    user_data[username] = hashed.decode('utf-8')
    with open ("user_auth.json", "w") as f:
         json.dump(user_data, f, indent=2)
    
    return True


while True:
    choice = input("Would you like to: \n1) Register \n2) Login \n3) Quit \n")

    if choice.lower() in ("1", "register"):
        if create_login():
            print("Account created\n")
        else:
            print("Username already exists\n")

    elif choice.lower() in ("2", "login"):
        if login_check():
            print("Login successful")
            break
        else:
            print("Invalid username or password\n")

    elif choice.lower() in ("3", "quit"):
        print("Have a good day")
        break

    else:
        print("Invalid choice\n")


