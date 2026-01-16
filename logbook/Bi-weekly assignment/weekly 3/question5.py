BAD_PASSWORDS = ["password", "letmein", "sesame", "hello", "justinbieber"]

while True:
    password1 = input("Enter new password: ")
    password2 = input("Confirm password: ")

    if password1 != password2:
        print("Error: Passwords do not match\n")
    elif len(password1) < 8 or len(password1) > 12:
        print("Error: Password must be between 8 and 12 characters\n")
    elif password1.lower() in BAD_PASSWORDS:
        print("Error: Password is too common\n")
    else:
        print("Password Set")
        break