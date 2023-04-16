import pytest


def test_create_course(universityApp):
    universityApp.create_course("CSC100", "Introduction to Programming", 1)
    assert universityApp.get_course("CSC100") == {
        "name": "Introduction to Programming",
        "lecturerID": 1,
    }

def test_create_course_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.create_course("CSC100", "Introduction to Programming", 1)
        universityApp.create_course("CSC100", "Introduction to Programming", 1)
    assert str(e.value) == "Course with code CSC100 already exists.\n"

def test_update_course(universityApp):
    universityApp.update_course("CSC100", "Introduction to Programming", 3)
    assert universityApp.get_course("CSC100") == {
        "name": "Introduction to Programming",
        "lecturerID": 3,
    }

def test_update_course_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.update_course("CSC300", "Introduction to Programming", 1)
    assert str(e.value) == "Course with code CSC300 does not exist.\n"

def test_get_course(universityApp):
    assert universityApp.get_course("CSC100") == {
        "name": "Introduction to Programming",
        "lecturerID": 3,
    }

def test_get_course_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.get_course("CSC300")
    assert str(e.value) == "Course with code CSC300 does not exist.\n"
