class UniversityApp:
    """The main class of the application."""

    def __init__(self):
        self.lecturers = {}
        self.students = {}
        self.courses = {}

    def create_lecturer(self, id: int, degree: str, firstName: str, lastName: str):
        """Creates a course lecturer.
        If a lecturer with the same id already exists, it will not be created."""

        if id in self.lecturers:
            print(f"Lecturer with id {id} already exists\n")
        else:
            self.lecturers[id] = {
                "degree": degree,
                "firstName": firstName,
                "lastName": lastName,
            }

    def create_course(self, code: str, name: str, lecturerID: int):
        """Creates a course.
        If a course with the same code already exists, it will not be created."""

        if code in self.courses:
            print(f"Course with code {code} already exists\n")
        else:
            self.courses[code] = {
                "name": name,
                "lecturerID": lecturerID,
            }

    def add_student_to_course(
        self, studentID: int, courseCode: str, firstName: str, lastName: str
    ):
        """Adds a student to a course.
        If the student is already in the course, it will not be added again."""

        if studentID in self.students:
            if courseCode in self.students[studentID]:
                print(
                    f"Student with id {studentID} is already in course {courseCode}\n"
                )
            else:
                self.students[studentID]["courses"].append(courseCode)
        else:
            self.students[studentID] = {
                "firstName": firstName,
                "lastName": lastName,
                "courses": {courseCode},
            }

    def print_course_info(self, courseCode: str):
        """Prints the course info to the console."""

        if courseCode in self.courses:
            course = self.courses[courseCode]
            lecturerID = course["lecturerID"]
            lecturer = self.lecturers[lecturerID]
            print(f"Course: {courseCode} - {course['name']}\n")
            print(
                f"Lecturer: {lecturer['degree']} {lecturer['firstName']} {lecturer['lastName']}\n"
            )
            print("Students:\n")
            for studentID in self.students:
                if courseCode in self.students[studentID]["courses"]:
                    student = self.students[studentID]
                    print(f"{student['firstName']} {student['lastName']}\n")
        else:
            print(f"Course with code {courseCode} does not exist")

    def add_grade(self, studentID: int, courseCode: str, grade: float):
        """Adds a grade to a student's course.
        If the student is not in the course, it will not be added."""

        if studentID in self.students:
            if courseCode in self.students[studentID]["courses"]:
                if self.students[studentID]["courses"][courseCode][grade] is not None:
                    print(
                        f"Student with id {studentID} already has a grade in course {courseCode}\n"
                    )
                else:
                    self.students[studentID]["courses"][courseCode] = grade
            else:
                print(f"Student with id {studentID} is not in course {courseCode}\n")
        else:
            print(f"Student with id {studentID} does not exist\n")

    def print_student_info(self, studentID: int):
        """Prints the student info to the console."""

        if studentID in self.students:
            student = self.students[studentID]
            print(f"Student: {student['firstName']} {student['lastName']}\n")
            print("Courses:\n")
            for courseCode in student["courses"]:
                course = self.courses[courseCode]
                print(f"{courseCode} - {course['name']}\n")
                print(f"Grade: {student['courses'][courseCode]}\n")
        else:
            print(f"Student with id {studentID} does not exist")

    def print_grades_for_course(self, courseCode: str):
        """Prints the grades for a course to the console."""

        if courseCode in self.courses:
            print(f"Course: {courseCode} - {self.courses[courseCode]['name']}\n")
            print("Grades:\n")
            for studentID in self.students:
                if courseCode in self.students[studentID]["courses"]:
                    print(
                        f"{self.students[studentID]['firstName']} {self.students[studentID]['lastName']} \
                        - {self.students[studentID]['courses'][courseCode]}\n"
                    )
        else:
            print(f"Course with code {courseCode} does not exist")

    def print_all_students(self):
        """Prints all students to the console."""

        print("Students:\n")
        for studentID in self.students:
            student = self.students[studentID]
            print(f"{student['firstName']} {student['lastName']}\n")
