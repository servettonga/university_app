import pytest


def test_create_student(universityApp):
    universityApp.create_student(1, "John", "Smith")
    assert universityApp.get_student(1) == {
        "firstName": "John",
        "lastName": "Smith",
        "courses": {}
    }

def test_create_student_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.create_student(1, "John", "Smith")

    assert str(e.value) == "Student with id 1 already exists.\n"

def test_update_student(universityApp):
    universityApp.update_student(1, "John", "Miller")
    assert universityApp.get_student(1) == {
        "firstName": "John",
        "lastName": "Miller",
        "courses": {}
    }

def test_update_student_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.update_student(3, "John", "Miller")

    assert str(e.value) == "Student with id 3 does not exist.\n"

def test_get_student(universityApp):
    assert universityApp.get_student(1) == {
        "firstName": "John",
        "lastName": "Miller",
        "courses": {}
    }

def test_get_student_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.get_student(3)

    assert str(e.value) == "Student with id 3 does not exist.\n"

def test_add_student_to_course(universityApp):
    universityApp.create_course("CS103", "Mathematical Foundations of Computing", 1)
    universityApp.add_student_to_course(1, "CS103")
    student = universityApp.get_student(1)
    assert student["courses"]["CS103"] == 'n/a'

def test_add_existing_student_to_course_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.add_student_to_course(1, "CS103")

    assert str(e.value) == "Student with id 1 is already in course CS103.\n"

def test_add_not_existing_student_to_course_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.add_student_to_course(10, "CS103")

    assert str(e.value) == "Student with id 10 does not exist.\n"
