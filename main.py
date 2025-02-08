def calc_average(grades):
    return sum(grades) / len(grades) if grades else 0


def class_of_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def input_student_data():
    name = input("Enter student's name: ").strip()
    grades = []

    for i in range(1, 4):
        while True:
            try:
                subject_grade = float(input(f"Enter grade for subject {i}: "))
                if 0 <= subject_grade <= 100:
                    grades.append(subject_grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return name, grades


def report(students):
    if not students:
        print("No student data available.")
        return

    print("\nStudents Grade Report:")
    print(f"{'Name':<20}{'Grades':<20}{'Average':<10}{'Classification':<15}")
    print("-" * 65)

    for name, grades, average, classification in students:
        grades_str = ", ".join(f"{g:.1f}" for g in grades)
        print(f"{name:<20}{grades_str:<20}{average:.2f}      {classification:<15}")


students = []

while True:
    print("\nStudent Grade Management System")
    print("1. Input student grades")
    print("2. Display student report")
    print("0. Exit")

    choice = input("Choose an operation (1, 2, or 0 to exit): ").strip()

    if choice == "0":
        print("Exiting the program...")
        break
    elif choice == "1":
        name, grades = input_student_data()
        average = calc_average(grades)
        classification = class_of_grade(average)
        students.append((name, grades, average, classification))
    elif choice == "2":
        report(students)
    else:
        print("Invalid choice. Please try again.")