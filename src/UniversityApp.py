class UniversityApp:
    """The main class of the application."""

    def __init__(self) -> None:
        self.__lecturers: dict = {}
        self.__students: dict = {}
        self.__courses: dict = {}

    def create_lecturer(self, id: int, degree: str, firstName: str, lastName: str) -> None:
        """Creates a course lecturer.
        If a lecturer with the same id already exists, it will not be created."""

        if id in self.__lecturers:
            raise Exception(f"Lecturer with id {id} already exists.\n")
        else:
            self.__lecturers[id] = {
                "degree": degree,
                "firstName": firstName,
                "lastName": lastName,
            }
            print(f"Lecturer with id {id} has been created.\n")

    def update_lecturer(self, id: int, degree: str, firstName: str, lastName: str) -> None:
        """Updates a course lecturer.
        If a lecturer with the same id does not exists, it will not be updated."""

        if id in self.__lecturers:
            self.__lecturers[id] = {
                "degree": degree,
                "firstName": firstName,
                "lastName": lastName,
            }
            print(f"Lecturer with id {id} has been updated.\n")
        else:
            raise Exception(f"Lecturer with id {id} does not exist.\n")

    def get_lecture(self, id: int) -> dict:
        """Returns a lecturer."""

        try:
            return self.__lecturers[id]
        except KeyError:
            raise Exception(f"Lecturer with id {id} does not exist.\n")

    def create_course(self, code: str, name: str, lecturerID: int) -> None:
        """Creates a course.
        If a course with the same code already exists, it will not be created."""

        if code in self.__courses:
            raise Exception(f"Course with code {code} already exists.\n")
        else:
            self.__courses[code] = {
                "name": name,
                "lecturerID": lecturerID,
            }
            print(f"Course with code {code} has been created.\n")

    def get_course(self, code: str) -> dict:
        """Returns a course."""

        try:
            return self.__courses[code]
        except KeyError:
            raise Exception(f"Course with code {code} does not exist.\n")

    def update_course(self, code: str, name: str, lecturerID: int) -> None:
        """Updates a course.
        If a course with the same code does not exists, it will not be updated."""

        if code in self.__courses:
            self.__courses[code] = {
                "name": name,
                "lecturerID": lecturerID,
            }
            print(f"Course with code {code} has been updated.\n")
        else:
            raise Exception(f"Course with code {code} does not exist.\n")

    def create_student(self, studentID: int, firstName: str, lastName: str) -> None:
        """Creates a student.
        If a student with the same id already exists, it will not be created."""

        if studentID in self.__students:
            raise Exception(f"Student with id {studentID} already exists.\n")
        else:
            self.__students[studentID] = {
                "firstName": firstName,
                "lastName": lastName,
                "courses": {},
            }
            print(f"Student with id {studentID} has been created.\n")

    def update_student(self, studentID: int, firstName: str, lastName: str) -> None:
        """Updates a student.
        If a student with the same id does not exists, it will not be updated."""

        if studentID in self.__students:
            self.__students[studentID] = {
                "firstName": firstName,
                "lastName": lastName,
                "courses": {},
            }
            print(f"Student with id {studentID} has been updated.\n")
        else:
            raise Exception(f"Student with id {studentID} does not exist.\n")

    def get_student(self, studentID: int) -> dict:
        """Returns a student."""

        try:
            return self.__students[studentID]
        except KeyError:
            raise Exception(f"Student with id {studentID} does not exist.\n")

    def add_student_to_course(self, studentID: int, courseCode: str) -> None:
        """Adds a student to a course.
        If the student is already in the course, it will not be added again."""

        if studentID in self.__students:
            if courseCode in self.__students[studentID]["courses"]:
                raise Exception(f"Student with id {studentID} is already in course {courseCode}.\n")
            else:
                self.__students[studentID]["courses"][courseCode] = 'n/a'
                print(f"Student with id {studentID} has been added to course {courseCode}.\n")
        else:
            raise Exception(f"Student with id {studentID} does not exist.\n")

    def add_grade(self, studentID: int, courseCode: str, grade: float) -> None:
        """Adds a grade to a student's course.
        If the student is not in the course, it will not be added."""

        if courseCode not in self.__courses:
            raise Exception(f"Course with code {courseCode} does not exist.\n")

        if studentID in self.__students:
            if courseCode in self.__students[studentID]["courses"]:
                if self.__students[studentID]["courses"][courseCode] != 'n/a':
                    raise Exception(
                        f"Student with id {studentID} already has a grade in course {courseCode}.\n"
                    )
                else:
                    self.__students[studentID]["courses"][courseCode] = grade
                    print(f"Grade {grade} has been added to student with id {studentID}.\n")
            else:
                raise Exception(f"Student with id {studentID} is not in course {courseCode}.\n")
        else:
            raise Exception(f"Student with id {studentID} does not exist.\n")

    def update_grade(self, studentID: int, courseCode: str, grade: float) -> None:
        """Changes a grade to a student's course.
        If the student is not in the course, it will not be updated."""

        if courseCode not in self.__courses:
            raise Exception(f"Course with code {courseCode} does not exist.\n")

        if studentID in self.__students:
            if courseCode in self.__students[studentID]["courses"]:
                if self.__students[studentID]["courses"][courseCode] == 'n/a':
                    raise Exception(
                        f"Student with id {studentID} does not have a grade in course {courseCode}.\n"
                    )
                else:
                    self.__students[studentID]["courses"][courseCode] = grade
                    print(f"Grade {grade} has been updated to student with id {studentID}.\n")
            else:
                raise Exception(f"Student with id {studentID} is not in course {courseCode}.\n")
        else:
            raise Exception(f"Student with id {studentID} does not exist.\n")

    def print_course_info(self, courseCode: str) -> None:
        """Prints the course info to the console."""

        if courseCode in self.__courses:
            course = self.__courses[courseCode]
            code = courseCode
            name = course["name"]
            lecturerID = course["lecturerID"]
            lecturer = self.__lecturers[lecturerID]
            degree = lecturer['degree']
            firstName = lecturer['firstName']
            lastName = lecturer['lastName']
            print(f"Course info:\n\tCode: {code}\n\tName: {name}")
            print(f"\tLecturer: {degree} {firstName} {lastName}\n")
            print("Students:")
            for studentID in self.__students:
                if courseCode in self.__students[studentID]["courses"]:
                    student = self.__students[studentID]
                    print(f"\t{student['firstName']} {student['lastName']} | Grade: {student['courses'][courseCode]}")
        else:
            raise Exception(f"Course with code {courseCode} does not exist.\n")

    def print_lecturer_info(self, lecturerID: int) -> None:
        """Prints the lecturer info to the console."""

        if lecturerID in self.__lecturers:
            lecturer = self.__lecturers[lecturerID]
            degree = lecturer['degree']
            firstName = lecturer['firstName']
            lastName = lecturer['lastName']
            print(f"Lecturer info:\n\tDegree: {degree}\n\tName: {firstName}\n\tSurname: {lastName}\n")
            print("Courses:")
            for courseCode in self.__courses:
                if self.__courses[courseCode]["lecturerID"] == lecturerID:
                    print(f"{courseCode} - {self.__courses[courseCode]['name']}")
        else:
            raise Exception(f"Lecturer with id {lecturerID} does not exist.\n")

    def print_student_info(self, studentID: int) -> None:
        """Prints the student info to the console."""

        if studentID in self.__students:
            student = self.__students[studentID]
            firstName = student['firstName']
            lastName = student['lastName']
            print(f"Student info:\n\tName: {firstName}\n\tSurname: {lastName}\n")
            print("Courses:")
            for courseCode in student["courses"]:
                courseName = self.__courses[courseCode]['name']
                grade = student['courses'][courseCode]
                print(f"\t{courseCode} - {courseName} | Grade: {grade}")
        else:
            raise Exception(f"Student with id {studentID} does not exist.\n")

    def print_grades_for_course(self, courseCode: str) -> None:
        """Prints the grades for a course to the console."""

        if courseCode in self.__courses:
            print(f"Grades for course: {courseCode} - {self.__courses[courseCode]['name']}\n")
            for studentID in self.__students:
                student = self.__students[studentID]
                firstName = student['firstName']
                lastName = student['lastName']
                if courseCode in student["courses"]:
                    print(f"{firstName} {lastName}: {student['courses'][courseCode]}\n")
        else:
            raise Exception(f"Course with code {courseCode} does not exist.\n")

    def print_all_students(self) -> None:
        """Prints all students to the console."""

        if self.__students:
            print("Students:\n")
            for studentID in self.__students:
                student = self.__students[studentID]
                print(f"{student['firstName']} {student['lastName']}\n")
        else:
            raise Exception("There are no students.\n")
