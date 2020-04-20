from student import Student
from instructor import Instructor
from exercise import Exercise
from cohort import Cohort
from nss_person import NSS_Person

students = []

minecraft = Exercise("Minecraft", "Java")
bank_account = Exercise("Bank Account", "C#")
capstone = Exercise("Capstone", "Javascript")
snake = Exercise("Snake Game", "Python")
fizz_buzz = Exercise("FizzBuzz", "Any")

C37 = Cohort("Day Cohort 37")
C38 = Cohort("Day Cohort 38")
C40 = Cohort("Day Cohort 40")

mac = Student("Mac", "Gibbons", "Mac Gibbons")
me = Student("Matthew", "Kroeger", "Matthew Kroeger")
coop = Student("Cooper", "Nichols", "Cooper Nichols")
frog = Student("Roxanne", "Nasraty", "Roxanne Nasraty")
students.extend([mac, me, coop, frog])

C37.assign_student(mac)
C38.assign_student(me)
C38.assign_student(coop)
C40.assign_student(frog)

steve = Instructor("Steve", "Brownlee", "coach", "Good Vibes")
jisie = Instructor("Jisie", "David", ":crown:", "Excitement")
bryan = Instructor("Bryan", "Nilsen", "Kickass High-Fiver", "High Fives")

C37.assign_instructor(steve)
C38.assign_instructor(jisie)
C40.assign_instructor(bryan)

steve.assign_exercise(mac, capstone)
steve.assign_exercise(mac, bank_account)
bryan.assign_exercise(frog, fizz_buzz)
bryan.assign_exercise(frog, capstone)

for student in C38.students:
    jisie.assign_exercise(student, minecraft)
    jisie.assign_exercise(student, snake)

for student in students:
    student_work = f"{student.first_name} {student.last_name} is working on "
    if len(student.exercises) > 1:
        for exercise in student.exercises:
            if exercise == student.exercises[-2]:
                student_work += f"{exercise.name} and "
            elif exercise == student.exercises[-1]:
                student_work += exercise.name
            else:
                student_work += f"{exercise.name}, "
    elif len(student.exercises) < 1:
        student_work += "nothing"
    else:
        student_work += student.exercises[0]
    print(student_work)
