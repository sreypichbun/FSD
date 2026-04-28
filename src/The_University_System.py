from student_controller import StudentControllerClass
from database_class import DatabaseClass
from admin_controller import AdminControllerClass

def University_System_Menu():
    database = DatabaseClass()
    
    while True:
        choice=input("University System: (A)dmin, (S)tudent, or X: ").upper()
        
        if choice =="A":
            admin_controller = AdminControllerClass(database)

            while True:
                admin_selection = Admin_System()
                

                if (admin_selection == 'c'): # Clear all data on students.data (done)
                    print("Clearing student database")
                    admin_controller.clear_student_data()
                  
                    
                elif (admin_selection == 'g'):  # grade grouping (Groups students by grade) 
                    # not ready yet (waiting for part c to complete)
                    #admin_controller.view_students_by_grade()
                    pass
                elif (admin_selection == 'p'): # pass/fail partition (Partition students to PASS/FAIL categories)
                    # not ready yet (waiting for part c to complete)
                    #admin_controller.categorize_students()
                    pass
                elif (admin_selection == 'r'): # Remove a student by ID (done)
                    admin_controller.remove_students()
                    
                elif (admin_selection == 's'):
                    # Show all students (done)
                    print("Student List")
                    admin_controller.view_students()
                    
                elif (admin_selection == 'x'):
                    break # exit admin menu, go back to main menu

        elif choice =="S":
            
            student_selection = Student_System()
            
            if (student_selection == 'r'):
                print("Student Sign Up")
                student_controller = StudentControllerClass(database)
                student_controller.register()
                print(database.students[0].name)
                
            elif (student_selection == 'l'):
                print("Student Log In")
                student_controller = StudentControllerClass(database)
                student_controller.login()
                
            elif (student_selection == 'x'):
                continue
            
        elif choice =="X":
            print("Thank You")
            break
        else:
            print("Error")    
                  
    
def Student_System() -> str:
    Choice = input("Student System (l/r/x): ").lower()
    return Choice


def Admin_System() -> str:
    Choice = input("Admin System (c/g/p/r/s/x): ").lower()
    return Choice
            
test = University_System_Menu()