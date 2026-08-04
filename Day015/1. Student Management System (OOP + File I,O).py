import json
import os

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self._load_students()

    def _load_students(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.filename, 'w') as f:
                json.dump([], f)
            return []

    def _save_students(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, name, age, grades):
        student = {"name": name, "age": age, "grades": grades}
        self.students.append(student)
        self._save_students()

    def remove_student(self, name):
        self.students = [s for s in self.students if s["name"].lower() != name.lower()]
        self._save_students()

    def get_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: sum(s["grades"]) / len(s["grades"]) if s["grades"] else 0)

    def get_average_age(self):
        if not self.students:
            return 0
        return sum(s["age"] for s in self.students) / len(self.students)
