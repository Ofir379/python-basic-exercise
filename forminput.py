username = input("Enter username: ")
password = input("Enter password: ")
email = input("Enter email: ")


if (len(username) > 0
    and len(password) >= 8 and any(ch.isdigit() for ch in password)
    and email.count("@") == 1 and email.endswith(".com")):
    print("Form valid")
else:
    print("Form invalid")


