from nss_person import NSS_Person

class Student(NSS_Person):
    def __init__(self, first_name, last_name, slack):
        super().__init__(first_name, last_name, slack)
        self.exercises = []
    
