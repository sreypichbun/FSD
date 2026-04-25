from Class_file import Student
import re #to use the regex

def register():
    name=input("Input name: ")
    while True:
        email=input("Input email in the format of @univeristy.com: ")
        password=input("Password Criteria\n 1.Start with upper case.\n 2. Contains at least 5 letters. \n 3. Followed by 3 or more digits.\n Input password: ")
        if validate_email(email) and validate_password(password):
            print("Email and Password formats acceptabble.")
            New_student=Student(name,email,password)
            print(f"Enrolling Student {New_student.name}")
            break
        else:
            print("Incorrect email or password format.")
    
    
    
    
    
    
 #Validate function   
def validate_email(email):
    email_pattern=r"[a-zA-Z]+\.[a-zA-Z]+@university\.com" #[] whatever can work, . must be exact, [] whatever can work, @univeristy exact, .com exact
    if re.match(email_pattern,email):
        return True
    else:
        return False
def validate_password(password):
    password_pattern=r"[A-Z][A-Za-z]{4,}[0-9]{3,}"
    if re.match(password_pattern,password):
        return True
    else:
        return False

