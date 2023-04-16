import pytest


def test_create_lecturer(universityApp):
    universityApp.create_lecturer(1, "Dr.", "John", "Smith")
    assert universityApp.get_lecture(1) == {
        "degree": "Dr.",
        "firstName": "John",
        "lastName": "Smith",
    }

def test_create_lecturer_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.create_lecturer(1, "Dr.", "John", "Smith")

    assert str(e.value) == "Lecturer with id 1 already exists.\n"

def test_update_lecturer(universityApp):
    universityApp.update_lecturer(1, "Dr.", "John", "Miller")
    assert universityApp.get_lecture(1) == {
        "degree": "Dr.",
        "firstName": "John",
        "lastName": "Miller",
    }

def test_update_lecturer_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.update_lecturer(3, "Dr.", "John", "Miller")
    assert str(e.value) == "Lecturer with id 3 does not exist.\n"

def test_get_lecture(universityApp):
    assert universityApp.get_lecture(1) == {
        "degree": "Dr.",
        "firstName": "John",
        "lastName": "Miller",
    }

def test_get_lecture_raises_exception(universityApp):
    with pytest.raises(Exception) as e:
        universityApp.get_lecture(3)
    assert str(e.value) == "Lecturer with id 3 does not exist.\n"
