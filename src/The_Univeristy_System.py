from student_controller import StudentControllerClass
from database_class import DatabaseClass

def University_System_Menu():
    database = DatabaseClass()
    
    while True:
        choice=input("University System: (A)dmin, (S)tudent, or X: ").upper()
        if choice =="A":
            # TODO Admin_System() TO BE BUILD
            pass
        elif choice =="S":
            
            student_selection = Student_System()
            if (student_selection == 'r'):
                print("Student Sign Up")
                
                student_controller = StudentControllerClass(database)
                student_controller.register()
                print(database.students[0].name)
                
            elif (student_selection == 'l'):
                pass
            
            elif (student_selection == 'x'):
                pass
            
        elif choice =="X":
            print("Thank You")
            break
        else:
            print("Error")    
                  
    
def Student_System() -> str:
    Choice = input("Student System (l/r/x): ").lower()
    return Choice
            
test = University_System_Menu()