import pytest


def test_print_course_info_not_raise(ready_set):
    try:
        ready_set.print_course_info("CS103")
    except Exception:
        pytest.fail("print_course_info raised an Exception unexpectedly!")

def test_print_course_info_raises(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.print_course_info("CX103")
    assert str(e.value) == "Course with code CX103 does not exist.\n"

def test_print_lecturer_info_not_raise(ready_set):
    try:
        ready_set.print_lecturer_info(1)
    except Exception:
        pytest.fail("print_lecturer_info raised an Exception unexpectedly!")

def test_print_lecturer_info_raises(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.print_lecturer_info(3)
    assert str(e.value) == "Lecturer with id 3 does not exist.\n"

def test_print_student_info_not_raise(ready_set):
    try:
        ready_set.print_student_info(1)
    except Exception:
        pytest.fail("print_student_info raised an Exception unexpectedly!")

def test_print_student_info_raises(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.print_student_info(10)
    assert str(e.value) == "Student with id 10 does not exist.\n"

def test_print_grades_for_course_not_raise(ready_set):
    try:
        ready_set.print_grades_for_course("CS103")
    except Exception:
        pytest.fail("print_grades_for_course raised an Exception unexpectedly!")

def test_print_grades_for_course_raises(ready_set):
    with pytest.raises(Exception) as e:
        ready_set.print_grades_for_course("CX103")
    assert str(e.value) == "Course with code CX103 does not exist.\n"

def test_print_all_students_not_raise(ready_set):
    try:
        ready_set.print_all_students()
    except Exception:
        pytest.fail("print_all_students raised an Exception unexpectedly!")

def test_print_all_students_raises(empty):
    with pytest.raises(Exception) as e:
        empty.print_all_students()
    assert str(e.value) == "There are no students.\n"
