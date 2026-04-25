from student_class import Student

class DatabaseClass:
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
    