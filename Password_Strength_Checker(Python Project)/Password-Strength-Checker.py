#Password Strength Checker

import re

#Password strength check conditions: min 8 chars, digit, uppercase , lowercase and special chars
def check_password_strength(password):
    if len(password) < 8:
        return "Weak! Password must be atleast 8 characters"
    if not any(char.isdigit() for char in password):
        return "Weak! Password must contain a digit"
    if not any(char.isupper() for char in password):
        return "Weak! Password must contain a uppercase character"
    if not any(char.islower() for char in password):
        return "Weak! Password must contain a lowercase character"
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{}|\\:;"<>,./~`]', password):
        return "Medium! Password must contain a special character"
    
    return "Strong! Password is secure!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Thank you for using the tool")
            break
        
        result = check_password_strength(password)
        print(result)

#Runs the password checker tool
if __name__ == "__main__":
    password_checker()
 
    

    
