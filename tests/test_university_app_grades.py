import pytest


def test_add_grade(ready_set):
    ready_set.add_grade(1, "CS103", 5.0)
    student = ready_set.get_student(1)
    assert student["courses"]["CS103"] == 5.0

def test_add_grade_already_set_raises_expection(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.add_grade(1, "CS103", 5.0)

    assert str(e.value) == "Student with id 1 already has a grade in course CS103.\n"

def test_add_grade_not_existing_student_raises_exception(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.add_grade(10, "CS103", 5.0)

    assert str(e.value) == "Student with id 10 does not exist.\n"

def test_add_grade_not_existing_course_raises_exception(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.add_grade(1, "CS104", 5.0)

    assert str(e.value) == "Course with code CS104 does not exist.\n"

def test_update_grade(ready_set):
    ready_set.update_grade(1, "CS103", 4.0)
    student = ready_set.get_student(1)
    assert student["courses"]["CS103"] == 4.0

def test_update_grade_not_existing_student_raises_exception(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.update_grade(10, "CS103", 5.0)

    assert str(e.value) == "Student with id 10 does not exist.\n"

def test_update_grade_not_existing_course_raises_exception(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.update_grade(1, "CS104", 5.0)

    assert str(e.value) == "Course with code CS104 does not exist.\n"
