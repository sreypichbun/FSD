from student_class import Student

class DatabaseClass:
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def find_student(self, email, password): # for log in finding student in the ls database
        for student in self.students:
            if student.email == email and student.password == password:
                return student
            return None
        
        # i think if u guts do like enrollment, or update point u guys also need to update the database class
     
    