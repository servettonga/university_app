import pytest
from src.UniversityApp import UniversityApp

universityApp = UniversityApp()

# test cases for the create_lecturer method
def test_create_lecturer():
    universityApp.create_lecturer(1, "Dr.", "John", "Smith")
    assert universityApp.lecturers[1] == {
        "degree": "Dr.",
        "firstName": "John",
        "lastName": "Smith",
    }


def test_create_lecturer_already_exists(capfd):
    universityApp.create_lecturer(101, "Dr.", "John", "Smith")
    universityApp.create_lecturer(101, "Dr.", "John", "Smith")
    out, err = capfd.readouterr()
    assert out == "Lecturer with id 101 already exists\n"


# test cases for the create_course method
# test cases for the add_student_to_course method
# test cases for the print_course_info method
# test cases for the add_grade method
# test cases for the print_student_info method
# test cases for the print_grades_for_course method
# test cases for the print_all_students method
