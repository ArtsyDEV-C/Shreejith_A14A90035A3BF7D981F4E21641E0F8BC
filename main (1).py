class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students_by_cgpa(students):
    sorted_students = sorted(students, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage
if __name__ == "__main__":
    # Creating instances of Student class
    student1 = Student("Alice", "A001", 3.8)
    student2 = Student("Bob", "B002", 3.5)
    student3 = Student("Charlie", "C003", 3.9)

    # List of student objects
    student_list = [student1, student2, student3]

    # Sorting students by CGPA
    sorted_students = sort_students_by_cgpa(student_list)

    # Printing sorted list
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")