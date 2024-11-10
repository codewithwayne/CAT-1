class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"\nGrades for {self.name} (ID: {self.student_id}):")
        if self.assignments:
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")
        else:
            print("No grades available.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) added to the course.")

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Assigned grade {grade} for '{assignment_name}' to {student.name}.")
                return
        print("Student not found.")

    def display_all_grades(self):
        print(f"\nAll students' grades in {self.course_name}:")
        for student in self.students:
            student.display_grades()


def main():
    instructor = Instructor("Samuel Githogori", "API")

    while True:
        print("\n--- Course Management System ---")
        print("1. Add a student")
        print("2. Assign a grade")
        print("3. Display all students and their grades")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == '2':
            student_id = input("Enter student's ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == '3':
            instructor.display_all_grades()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
