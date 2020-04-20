from nss_person import NSS_Person

class Instructor(NSS_Person):
    def __init__(self, first_name, last_name, slack, specialty):
        super().__init__(first_name, last_name, slack)
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
        