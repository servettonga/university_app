import sys

import src.controller as ct
from src.UniversityApp import UniversityApp

universityApp = UniversityApp()

def main():
    choices: dict[int, str] = {
        1: "Create a new lecturer",
        2: "Create a new student",
        3: "Create a new course",
        4: "Add student to a course",
        5: "Add grade to a course",
        6: "Update lecturer",
        7: "Update student",
        8: "Update course",
        9: "Update grade",
        10: "Lecturer information",
        11: "Student information",
        12: "Course information",
        0: "Exit"}

    while True:
        ct.clear()
        print(ct.header)
        for choice in choices:
            print(f"{choice}: {choices[choice]}")

        choice = int(input("\nEnter your choice: "))

        print(f"\n{choice}: {choices[choice]}")

        try:
            match choice:
                case 1:
                    ct.create_lecturer(universityApp)
                case 2:
                    ct.create_student(universityApp)
                case 3:
                    ct.create_course(universityApp)
                case 4:
                    ct.add_student_to_course(universityApp)
                case 5:
                    ct.add_grade(universityApp)
                case 6:
                    ct.update_lecturer(universityApp)
                case 7:
                    ct.update_student(universityApp)
                case 8:
                    ct.update_course(universityApp)
                case 9:
                    ct.update_grade(universityApp)
                case 10:
                    ct.print_lecturer(universityApp)
                case 11:
                    ct.print_student(universityApp)
                case 12:
                    ct.print_course(universityApp)
                case 0:
                    sys.exit(0)
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Invalid input!")
            ct.clear(1)

if __name__ == "__main__":
    main()
