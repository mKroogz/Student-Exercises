from nss_person import NSS_Person

class Student(NSS_Person):
    def __init__(self, first_name, last_name, slack, cohort):
        super().__init__(first_name, last_name, slack)
        self.cohort = cohort
        self.exercises = []
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'