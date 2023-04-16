# Methods to use in the main program
import os
import time

from .UniversityApp import UniversityApp

header = """
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |U|N|I|V|E|R|S|I|T|Y| |A|P|P|
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""
def clear(n=0):
    time.sleep(n)
    os.system("cls" if os.name == "nt" else "clear")

def create_lecturer(app: UniversityApp):
    lecturer_id = int(input("Enter lecturer id: "))
    title = input("Enter title: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    if (lecturer_id and title and first_name and last_name)\
            and (str(lecturer_id).isdecimal() and title.isalpha() and first_name.isalpha() and last_name.isalpha()) :
        try:
            app.create_lecturer(id=lecturer_id, title=title, first_name=first_name, last_name=last_name)
        except Exception as e:
            print(e)
    else:
        print("You must enter a valid title, first name and last name.")
    input("Press enter to continue...")

def create_student(app: UniversityApp):
    student_id = int(input("Enter student id: "))
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    if (student_id and first_name and last_name) and (first_name.isalpha() and last_name.isalpha()) :
        try:
            app.create_student(studentID=student_id, firstName=first_name, lastName=last_name)
        except Exception as e:
            print(e)
    else:
        print("You must enter a valid first name and last name.")
    input("Press enter to continue...")

def create_course(app: UniversityApp):
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")
    lecturer_id = int(input("Enter lecturer id: "))
    if (course_code and course_name and lecturer_id) and course_code.isalnum() :
        try:
            app.create_course(code=course_code, name=course_name, lecturer_id=lecturer_id)
        except Exception as e:
            print(e)
    else:
        print("You must enter a valid course code, course name and lecturer id.")
    input("Press enter to continue...")

def add_student_to_course(app: UniversityApp):
    student_id = int(input("Enter student id: "))
    course_code = input("Enter course code: ")
    try:
        app.add_student_to_course(studentID=student_id, courseCode=course_code)
    except Exception as e:
        print(e)
    input("Press enter to continue...")

def update_lecturer(app: UniversityApp):
    lecturer_id = int(input("Enter lecturer id: "))
    title = input("Enter title: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    if (lecturer_id and title and first_name and last_name)\
            and (str(lecturer_id).isdecimal() and title.isalpha() and first_name.isalpha() and last_name.isalpha()) :
        try:
            app.update_lecturer(id=lecturer_id, title=title, first_name=first_name, last_name=last_name)
        except Exception as e:
            print(e)
    else:
        print("You must enter a valid title, first name and last name.")
    input("Press enter to continue...")

def update_student(app: UniversityApp):
    student_id = int(input("Enter student id: "))
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    if (student_id and first_name and last_name) and\
            (str(student_id).isdecimal() and first_name.isalpha() and last_name.isalpha()):
        try:
            app.update_student(studentID=student_id, firstName=first_name, lastName=last_name)
        except Exception as e:
            print(e)
    else:
        print("You must enter a valid first name and last name.")
    input("Press enter to continue...")

def update_course(app: UniversityApp):
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")
    lecturer_id = int(input("Enter lecturer id: "))
    if (course_code and course_name and lecturer_id) and course_code.isalnum() :
        try:
            app.update_course(code=course_code, name=course_name, lecturer_id=lecturer_id)
        except Exception as e:
            print(e)
    else:
        print("You must enter a valid course code, course name and lecturer id.")
    input("Press enter to continue...")

def add_grade(app: UniversityApp):
    student_id = int(input("Enter student id: "))
    course_code = input("Enter course code: ")
    grade = float(input("Enter grade: "))
    if (student_id and course_code and grade) and\
            (str(student_id).isdecimal() and course_code.isalnum()) :
        try:
            app.add_grade(studentID=student_id, courseCode=course_code, grade=grade)
        except Exception as e:
            print(e)
    else:
        print("You must enter a valid student id, course code and grade.")
    input("Press enter to continue...")

def update_grade(app: UniversityApp):
    student_id = int(input("Enter student id: "))
    course_code = input("Enter course code: ")
    grade = float(input("Enter grade: "))
    if (student_id and course_code and grade) and\
            (str(student_id).isdecimal() and course_code.isalnum()) :
        try:
            app.update_grade(studentID=student_id, courseCode=course_code, grade=grade)
        except Exception as e:
            print(e)
    else:
        print("You must enter a valid student id, course code and grade.")
    input("Press enter to continue...")

def print_lecturer(app: UniversityApp):
    lecturer_id = int(input("Enter lecturer id: "))
    try:
        app.print_lecturer_info(lecturerID=lecturer_id)
    except Exception as e:
        print(e)
    input("Press enter to continue...")

def print_student(app: UniversityApp):
    student_id = int(input("Enter student id: "))
    try:
        app.print_student_info(studentID=student_id)
    except Exception as e:
        print(e)
    input("Press enter to continue...")

def print_course(app: UniversityApp):
    course_code = input("Enter course code: ")
    try:
        app.print_course_info(courseCode=course_code)
    except Exception as e:
        print(e)
    input("Press enter to continue...")
