from admin_class import Admin
from database_class import DatabaseClass

class AdminControllerClass:
    def __init__(self, database):
        self.database = database

    def view_students(self):
        students = self.database.students

        if len(students) == 0:
            print("No students registered")
        else:
            for student in students:
                print(f"{student.name} :: {student.studentID} --> Email: {student.email}")

        

    def remove_students(self):
        student_id = input("Remove by ID: ")

        found = False

        for student in self.database.students:
            if str(student.studentID) == student_id:
                self.database.students.remove(student)
                found = True
                break

        if found:
            self.database.save_students()
            print(f"Removing Student {student_id} Account")
        else:
            print(f"Student {student_id} does not exist")

    def clear_student_data(self):
        clear_decision = input("Are you sure you want to clear the database (Y)ES/(N)O: ").upper()

        if clear_decision == "Y":
            self.database.clear_students()
            print("Students data cleared")

        elif clear_decision == "N":
            print("Cancelled")

        else:
            print("Invalid option")