def add_grades(students_base):
    student_name = input("Enter student name: ")
    for student in students_base:
        if student["name"] == student_name:
            while True:
                feedback = input("Enter a grade (or 'done' to finish):")
                if feedback == "done":
                    break
                try:
                    grade = float(feedback)
                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                    else:
                        print("Invalid grade. Try adain!")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            return
    print("Student you are looking for does not exist")


def add_student(students_base):
    student_name = input("Enter student name: ")
    for student in students_base:
        if student_name.lower() == student["name"].lower():
            print("Student already exists")
            return
    student_profile = {"name": student_name, "grades": []}
    students_base.append(student_profile)

def get_student_average(student):
    if student["grades"]:
        return sum(student["grades"])/len(student["grades"])
    return "N/A"

def get_info(students_base, parameter):
    max_average = 0
    min_average = 100
    overall_average = 0
    count = 0
    for student in students_base:
        if student["grades"]:
            count += 1
            student_average = get_student_average(student)
            if student_average != "N/A":
                overall_average += student_average
                if max_average < student_average:
                    max_average = student_average
                if min_average > student_average:
                    min_average = student_average
    if count > 0:
        overall_average /= count
    else:
        overall_average = 0
    if parameter == "overall_average":
        return overall_average
    elif parameter == "max_average":
        return max_average
    elif parameter == "min_average":
        return min_average

def create_and_print_profile(students_base):
    print("--- Student Report ---")
    if students_base != []:
        max_average = get_info(students_base, "max_average")
        min_average = get_info(students_base, "min_average")
        overall_average = get_info(students_base, "overall_average")
        for student in students_base:
            student_average = get_student_average(student)
            print(f"{student["name"]}'s average grade is {student_average}")
        print("---------------------")
        print(f"Max Average: {max_average}")
        print(f"Min Average: {min_average}")
        print(f"Overall Average: {overall_average}")
    else:
        print("There are no students")

def is_empty(students_base):
    for student in students_base:
        if student["grades"]:
            return False
    return True

def find_and_print_top_student(students_base):
    empty = is_empty(students_base)
    if not students_base:
        print("There are no students")
        return
    if not empty:
        top_student = max(students_base, key = lambda st: sum(st["grades"])/len(st["grades"]))
        top_average = get_student_average(top_student)
        print(f"The student with the highest average is {top_student['name']} with a grade of {top_average:.1f}.")
    else:
        print("No students with grades available")

def main():
    students_base = []
    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student"
              "\n2. Add grades for a student"
              "\n3. Generate a full report"
              "\n4. Find the top student"
              "\n5. Exit program")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                add_student(students_base)
            elif choice == 2:
                add_grades(students_base)
            elif choice == 3:
                create_and_print_profile(students_base)
            elif choice == 4:
                find_and_print_top_student(students_base)
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Incorrect choice. Please enter 1-5.")
        except ValueError:
            print("Invalid input. Please try a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()