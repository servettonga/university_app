import pytest

from src.UniversityApp import UniversityApp


@pytest.fixture(scope="module")
def universityApp() -> UniversityApp:
    return UniversityApp()

@pytest.fixture(scope="module")
def ready_set():
    universityApp = UniversityApp()
    universityApp.create_lecturer(1, "Dr.", "John", "Smith")
    universityApp.create_student(1, "Junior", "Smith")
    universityApp.create_course("CS103", "Mathematical Foundations of Computing", 1)
    universityApp.add_student_to_course(1, "CS103")
    return universityApp

@pytest.fixture(scope="module")
def empty():
    universityApp = UniversityApp()
    return universityApp
