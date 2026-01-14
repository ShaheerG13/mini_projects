import re

def email_checker(email):
    valid_format = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'

    if re.fullmatch(valid_format, email, re.IGNORECASE):
        print("Valid\n")
    else:
        print("Invalid\n")

while True:
    email = input("Enter in your email: ")
    email_checker(email)
