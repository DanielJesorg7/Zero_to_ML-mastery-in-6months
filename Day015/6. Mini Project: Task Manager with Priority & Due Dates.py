import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, name, priority, due_date):
        task = {
            "name": name,
            "priority": int(priority),
            "due_date": due_date  # Format expected: YYYY-MM-DD
        }
        self.tasks.append(task)
        self._save()

    def list_tasks(self):
        # Sorts tasks dynamically by priority (1 to 5)
        return sorted(self.tasks, key=lambda x: x['priority'])

    def mark_complete(self, name):
        self.tasks = [t for t in self.tasks if t["name"].lower() != name.lower()]
        self._save()

    def show_overdue(self):
        today = datetime.today().date()
        overdue = []
        for t in self.tasks:
            try:
                task_date = datetime.strptime(t["due_date"], "%Y-%m-%d").date()
                if task_date < today:
                    overdue.append(t)
            except ValueError:
                continue
        return overdue

def menu():
    manager = TaskManager()
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task complete")
        print("4. Show overdue tasks")
        print("5. Save/load Status (Auto-handled)")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter task name: ")
            priority = input("Enter priority (1-5): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            manager.add_task(name, priority, due_date)
            print("Task added successfully.")
        elif choice == '2':
            tasks = manager.list_tasks()
            print("\nTasks (Sorted by Priority):")
            for t in tasks:
                print(f"- {t['name']} [Priority: {t['priority']}, Due: {t['due_date']}]")
        elif choice == '3':
            name = input("Enter the name of the task to complete: ")
            manager.mark_complete(name)
            print("Task updated.")
        elif choice == '4':
            overdue = manager.show_overdue()
            print("\nOverdue Tasks:")
            for t in overdue:
                print(f"- {t['name']} [Due: {t['due_date']}]")
        elif choice == '5':
            print("Tasks are automatically persisted to 'tasks.json'.")
        elif choice == '6':
            print("Exiting application.")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    menu()
