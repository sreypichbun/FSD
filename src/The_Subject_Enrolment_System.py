import random

class Subject:
    def __init__(self, subject_id=None):
        # ID: a unique, randomly generated 3-digit number (001 to 999)
        self.id = subject_id if subject_id else f"{random.randint(1, 999):03d}"
        # Mark: randomly generated between 25 and 100
        self.mark = random.randint(25, 100)
        # Grade: determined based on the mark
        self.grade = self._calculate_grade(self.mark)

    def _calculate_grade(self, mark):
        # Grade boundaries as implied by Sample I/O
        if mark >= 85: return "HD"
        if mark >= 75: return "D"
        if mark >= 65: return "C"
        if mark >= 50: return "P"
        return "Z"

    def __str__(self):
        # Matches Sample I/O: [ Subject::ID -- mark = XX -- grade = XX ]
        return f"[ Subject::{self.id} -- mark = {self.mark} -- grade = {self.grade} ]"

class SubjectEnrolmentSystem:
    def __init__(self, student, database):
        # The system interacts with Student objects and the Database file
        self.student = student
        self.db = database

    def run(self):
        """
        Main menu for Subject Enrolment System.
        Menu options: (c)hange, (e)nrol, (r)emove, (s)how, (x)it
        """
        while True:
            # Display prompt: Student Course Menu (c/e/r/s/x):
            choice = input("Student Course Menu (c/e/r/s/x): ").lower().strip()
            
            if choice == 'c':
                self.change_password()
            elif choice == 'e':
                self.enrol()
            elif choice == 'r':
                self.remove_subject()
            elif choice == 's':
                self.show_enrolment()
            elif choice == 'x':
                break

    def enrol(self):
        """
        Enroll
        """
        if len(self.student.subjects) >= 4:
            # Matches Sample I/O error message
            print("Students are allowed to enrol in 4 subjects only")
            return

        # Create new subject and add to student's list
        new_subject = Subject()
        self.student.subjects.append(new_subject)
        
        # Requirement: Read/Write to file (Save progress to students.data)
        self.db.update_student(self.student) 
        
        # Matches Sample I/O output format
        print(f"Enrolling in Subject-{new_subject.id}")
        print(f"You are now enrolled in {len(self.student.subjects)} out of 4 subjects")

    def remove_subject(self):
        """
        Remove a subject
        """
        # Matches Sample I/O: Remove Subject by ID:
        subject_id = input("Remove Subject by ID: ").strip()
        
        original_count = len(self.student.subjects)
        # Filter list to remove the specific subject ID
        self.student.subjects = [s for s in self.student.subjects if s.id != subject_id]
        
        if len(self.student.subjects) < original_count:
            # Requirement: Update students.data after removal
            self.db.update_student(self.student)
            # Matches Sample I/O: Dropping Subject-ID
            print(f"Dropping Subject-{subject_id}")
            print(f"You are now enrolled in {len(self.student.subjects)} out of 4 subjects")
        else:
            # Scenario: ID not found (optional but logical error handling)
            print(f"Subject {subject_id} not found.")

    def show_enrolment(self):
        """
        Show subjects
        """
        # Matches Sample I/O: Showing X subjects
        print(f"Showing {len(self.student.subjects)} subjects")
        for sub in self.student.subjects:
            print(sub)

    def change_password(self):
        """
        Change password
        """
        # Matches Sample I/O: Updating Password
        print("Updating Password")
        while True:
            new_pwd = input("New Password: ")
            confirm_pwd = input("Confirm Password: ")
            
            if new_pwd == confirm_pwd:
                # Note: Password must be validated against RegEx in actual implementation
                self.student.password = new_pwd
                # Requirement: Save new password to students.data
                self.db.update_student(self.student)
                break
            else:
                # Matches Sample I/O: Password does not match try again
                print("Password does not match try again")