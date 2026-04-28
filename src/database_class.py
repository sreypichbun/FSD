import pickle
from student_class import Student

class DatabaseClass:
    def __init__(self):
        self.students = []
        self.filename = "students.data"

        try:
            self.load_students()
        except:
            self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def find_student(self, email, password):
        for student in self.students:
            if student.email == email and student.password == password:
                return student
        return None

    def load_students(self):
        with open(self.filename, "rb") as file:
            self.students = pickle.load(file)

    def save_students(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.students, file)

    def clear_students(self):
        self.students = []
        self.save_students()