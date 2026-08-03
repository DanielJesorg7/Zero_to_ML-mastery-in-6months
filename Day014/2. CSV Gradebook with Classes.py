import csv

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = [float(g) for g in grades]

class Gradebook:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        name = row[0]
                        grades = row[1:]
                        self.students.append(Student(name, grades))
        except FileNotFoundError:
            print(f"Warning: {self.filename} not found. Starting with an empty gradebook.")
        except Exception as e:
            print(f"Error loading file: {e}")

    def add_student(self, name, grades):
        self.students.append(Student(name, grades))

    def calculate_class_average(self):
        total_sum = 0
        total_count = 0
        for student in self.students:
            total_sum += sum(student.grades)
            total_count += len(student.grades)
        return total_sum / total_count if total_count > 0 else 0

    def save_to_csv(self):
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                for student in self.students:
                    writer.writerow([student.name] + student.grades)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")
