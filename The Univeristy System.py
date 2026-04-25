from register import register
def University_System_Menu():
    while True:
        choice=input("University System: (A)dmin, (S)tudent, or X: ").upper()
        if choice =="A":
            #Admin_System() TO BE BUILD
            pass
        elif choice =="S":
            Student_System()
            pass
        elif choice =="X":
            print("Thank You")
            break
        else:
            print("Error")    
                  
    
def Student_System():
    while True:
        Choice=input("Student System (l/r/x): ").lower()
        if Choice=="r":
            register()
            pass
        elif Choice=="l":
            #Student_Sign_In
            pass
        elif Choice =="x":
            break
            
University_System_Menu()