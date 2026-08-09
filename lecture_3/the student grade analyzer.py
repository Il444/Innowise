def add_grades(students_base):
    student_name = input("Enter student name: ")
    for student in students_base:
        if student["name"] == student_name:
            grade = int(input("Enter a grade (or 'done' to finish):"))
            if 0 <= grade <= 100:
                student["grades"].append(grade)
            else:
                print("Invalid grade. Try adain!")
        else:
            print("Student you are looking for does not exist")

def add_student(students_base):
    student_name = input("Enter student name: ")
    if student_name in students_base:
        print("Student already exists")
    else:
        student_profile = {"name": student_name, "grades": []}
        students_base.append(student_profile)

def get_student_average(student):
    if student["grades"] != []:
        student_average = 0
        for grade in student["grades"]:
            student_average += grade
        student_average /= len(student["grades"])
    else:
        student_average = "N/A"
    return student_average

def get_info(students_base, parameter):
    max_average = 0
    min_average = 100
    overall_average = 0
    for student in students_base:
        if student["grades"] != []:
            for student in students_base:
                student_average = get_student_average(student)
                overall_average += student_average
                if max_average < student_average:
                    max_average = student_average
                if min_average > student_average:
                    max_average = student_average
        else:
            student_average = "N/A"
    overall_average /= len(students_base["name"])
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
            for student in students_base:
                student_average = get_student_average(student)
                print(f"{student["name"]}'s average grade is {student_average}")
        print("---------------------")
        print(f"Max Average: {max_average}")
        print(f"Min Average: {min_average}")
        print(f"Overall Average: {overall_average}")
    else:
        print("There are no students")

def find_and_print_top_student(students_base):
    max_average = get_info(students_base, "max_average")
    for student in students_base:
        student_average = get_student_average(student)
        if max_average == student_average:
            print(f"The student with the highest average is {student['name']} with a grade 0f {max_average}")

def main():
    students_base = []
    print("--- Student Grade Analyzer ---")
    while True:
        print("1. Add a new student"
              "2. Add grades for a student"
              "3. Generate a full report"
              "4. Find the top student"
              "5. Exit program")
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
        except ValueError:
            print("Invalid input. Please try a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()