import random

class Student:
    def __init__(self,name,email,password):
        self.name= name
        self.email=email
        self.password=password
        self.studentID=random.randint(1,999999)
        self.subject=[]   
        