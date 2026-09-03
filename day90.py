class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(
            f"ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Marks: {self.marks}"
        )


students = {}


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        if student_id in students:
            print("Student ID already exists.")
        else:
            students[student_id] = Student(student_id, name, marks)
            print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for student in students.values():
                student.display()

    elif choice == "3":
        student_id = input("Enter student ID to search: ")

        if student_id in students:
            students[student_id].display()
        else:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter student ID to update: ")

        if student_id in students:
            name = input("Enter new name: ")
            marks = float(input("Enter new marks: "))

            students[student_id].name = name
            students[student_id].marks = marks

            print("Student updated successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        student_id = input("Enter student ID to delete: ")

        if student_id in students:
            del students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")