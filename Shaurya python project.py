class Student:
    def _init_(self, name, roll_number, marks1,marks2):
        self.name = name
        self.roll_number = roll_number
        self.marks1 = marks1
        self.marks2 = marks2
class StudentManagementSystem:
    def _init_(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter student roll number: ")
        marks1 = input("Enter student Marks1: ")
        marks2 = input("Enter student Marks2: ")
        student = Student(name, roll_number, marks1, marks2)
        self.students.append(student)
        print(f"Student '{name}' added successfully!")

    def search_student(self):
        roll_number = input("Enter student roll number: ")
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student found:")
                print(f"Name: {student.name}")
                print(f"Roll Number: {student.roll_number}")
                print(f"Marks1: {student.marks1}")
                print(f"Marks2: {student.marks2}")
                return
        print(f"Student with roll number '{roll_number}' not found.")

    def remove_student(self):
        roll_number = input("Enter student roll number: ")
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student with roll number '{roll_number}' removed successfully!")
                return
        print(f"Student with roll number '{roll_number}' not found.")

    def update_student(self):
        roll_number = input("Enter student roll number: ")
        for student in self.students:
            if student.roll_number == roll_number:
                print("Enter new student details:")
                name = input("Name: ")
                marks1 = input("Marks1: ")
                marks2 = input("Marks2: ")
                student.name = name
                student.marks1 = marks1
                student.marks2 = marks2
                print(f"Student with roll number '{roll_number}' updated successfully!")
                return
        print(f"Student with roll number '{roll_number}' not found.")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        print("Student List:")
        print("--------------")
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Roll Number: {student.roll_number}")
            print(f"Marks1: {student.marks1}")
            print(f"Marks2: {student.marks2}")
            print("--------------")


obj = StudentManagementSystem()

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("------------------------")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Remove Student")
    print("4. Update Student")
    print("5. Display Students")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        obj.add_student()
    elif choice == "2":
        obj.search_student()
    elif choice == "3":
        obj.remove_student()
    elif choice == "4":
        obj.update_student()
    elif choice == "5":
        obj.display_students()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")