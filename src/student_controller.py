import re
from student_class import Student
from database_class import DatabaseClass

class StudentControllerClass:
    def __init__(self, database):
        self.database = database
    
    def register(self):
        name = input("Input name: ")
        while True:
            
            email = input("Input email in the format of @univeristy.com: ")
            password = input("Password Criteria\n 1.Start with upper case.\n 2. Contains at least 5 letters. \n 3. Followed by 3 or more digits.\n Input password: ")
            
            if self.validate_email(email) and self.validate_password(password):
                print("Email and Password formats acceptabble.")
                new_student= Student(name,email,password)
                print(f"Enrolling Student {new_student.name}")
                
                self.database.add_student(new_student)
                break
            
            else:
                print("Incorrect email or password format.")
                
    def login(self):
        email = input("Email: ")
        password= input("Password: ")
        
        student = None
        
        if self.validate_email(email) and self.validate_password(password):
            print("email and password format accpetable")
            student = self.database.find_student(email,password)
            if student:
                self.student_course_menu()
            else:
                print("Student does not exist.")
        else:
            print("Incorrect email or password format.")
        
                
    #Validate function   
    def validate_email(self, email):
        email_pattern=r"[a-zA-Z]+\.[a-zA-Z]+@university\.com" #[] whatever can work, . must be exact, [] whatever can work, @univeristy exact, .com exact
        if re.match(email_pattern, email):
            return True
        else:
            return False
        
    def validate_password(self, password):
        password_pattern=r"[A-Z][A-Za-z]{4,}[0-9]{3,}"
        if re.match(password_pattern, password):
            return True
        else:
            return False
        
     # Need to link to sarah enrollment part but i think she has the same mennu done in her part 
  
    def student_course_menu(self):
        while True:
            choice = input("Student Course Menu (c/e/r/s/x)").lower()
        
            if choice =="c":
                print('c')
            elif choice =="e":
                print("e")
            elif choice =='r':
                print("r")
            elif choice =="s":
                print("s")
            elif choice =="x":
                print("x")
                break
            else:
                print("iNVALID")
    