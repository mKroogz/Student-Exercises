class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors = []
    
    def assign_student(self, student):
        student.cohort = self.name
        self.students.append(student)

    def assign_instructor(self, instructor):
        instructor.cohort = self.name
        self.instructors.append(instructor)