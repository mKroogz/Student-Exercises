from nss_person import NSS_Person

class Instructor(NSS_Person):
    def __init__(self, first_name, last_name, slack, specialty, cohort):
        super().__init__(first_name, last_name, slack)
        self.cohort = cohort
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
        
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'