import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        # Contains the absolute path to your database file
        self.db_path = "/home/kroogz/workspace/python/StudentExercises/studentexercises.db"

    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])
            # conn.row_factory = lambda cursor, row: Student(*row)

            db_cursor = conn.cursor()

            execute_query = db_cursor.execute("""
            SELECT s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.CohortId,
                c.Name
            FROM Student s
            JOIN Cohort c ON s.CohortId = c.Id
            ORDER BY s.CohortId
            """)

            # print(execute_query)

            all_students = db_cursor.fetchall()

            # print(all_students)

            # When there is no row_factory function defined, we get a list of tuples
            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # We have a row_factory function specified. That lambda takes each tuple and returns an instance of the Student class
            for student in all_students:
                print(student)

            # db_cursor.execute("SELECT i.FirstName, i.LastName FROM Instructor i")

            # all_instructors = db_cursor.fetchall()

            # print(all_instructors)

    def all_instructors(self):
        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[5], row[6])
            # conn.row_factory = lambda cursor, row: Instructor(*row)

            db_cursor = conn.cursor()

            execute_query = db_cursor.execute("""
            SELECT i.Id,
                i.First_Name,
                i.Last_Name,
                i.Slack_Handle,
                i.CohortId,
                i.Speciality,
                c.Name
            FROM Instructor i
            JOIN Cohort c ON i.CohortId = c.Id
            ORDER BY i.CohortId
            """)

            # print(execute_query)

            all_instructors = db_cursor.fetchall()

            # print(all_instructors)

            # When there is no row_factory function defined, we get a list of tuples
            # for instructor in all_instructors:
            #     print(f'{instructor[1]} {instructor[2]} is in {instructor[5]}')

            # We have a row_factory function specified. That lambda takes each tuple and returns an instance of the instructor class
            for instructor in all_instructors:
                print(instructor)

            # db_cursor.execute("SELECT i.FirstName, i.LastName FROM Instructor i")

            # all_instructors = db_cursor.fetchall()

            # print(all_instructors)

    def all_cohorts(self):
        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])

            db_cursor = conn.cursor()

            execute_query = db_cursor.execute("""
            SELECT c.Id,
                c.Name
            FROM Cohort c
            """)

            # print(execute_query)

            all_cohorts = db_cursor.fetchall()

            # print(all_cohorts)

            # When there is no row_factory function defined, we get a list of tuples
            # for student in all_cohorts:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # We have a row_factory function specified. That lambda takes each tuple and returns an instance of the Student class
            for cohort in all_cohorts:
                print(cohort)

            # db_cursor.execute("SELECT i.FirstName, i.LastName FROM Instructor i")

            # all_instructors = db_cursor.fetchall()

            # print(all_instructors)

    def all_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            execute_query = db_cursor.execute("""
            SELECT e.Id,
                e.Name,
                e.Exercise_Language
            FROM Exercise e
            """)

            # print(execute_query)

            all_exercises = db_cursor.fetchall()

            # print(all_exercises)

            # When there is no row_factory function defined, we get a list of tuples
            # for student in all_exercises:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # We have a row_factory function specified. That lambda takes each tuple and returns an instance of the Student class
            for exercise in all_exercises:
                print(exercise)

            # db_cursor.execute("SELECT i.FirstName, i.LastName FROM Instructor i")

            # all_instructors = db_cursor.fetchall()

            # print(all_instructors)

    def choose_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])

            db_cursor = conn.cursor()

            execute_query = db_cursor.execute("""
            SELECT e.Id,
                e.Name,
                e.Exercise_Language
            FROM Exercise e
            """)

            # print(execute_query)

            all_exercises = db_cursor.fetchall()

            print("Which Language?")

            print("1. Javascript")
            print("2. C#")
            print("3. Python")
            choice = 0
            while not choice:
                choice = input(">> ")
                if choice == "1":
                    choice = "Javascript"
                elif choice == "2":
                    choice = "C#"
                elif choice == "3":
                    choice = "Python"
                else:
                    print("Choose a number 1-3")
                    choice = 0

            def check_exercise(exercise, language):
                if exercise.language == language:
                    print(exercise)


            # print(all_exercises)

            # When there is no row_factory function defined, we get a list of tuples
            # for student in all_exercises:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # We have a row_factory function specified. That lambda takes each tuple and returns an instance of the Student class
            for exercise in all_exercises:
                check_exercise(exercise, choice)

            # db_cursor.execute("SELECT i.FirstName, i.LastName FROM Instructor i")

            # all_instructors = db_cursor.fetchall()

            # print(all_instructors)


reports = StudentExerciseReports()
reports.all_instructors()