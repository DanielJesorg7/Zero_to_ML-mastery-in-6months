import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def add(self, name, phone, email=""):
        self.contacts.append({"name": name, "phone": phone, "email": email})
        self._save()

    def delete(self, name):
        self.contacts = [c for c in self.contacts if c["name"].lower() != name.lower()]
        self._save()

    def search(self, partial_name):
        return [c for c in self.contacts if partial_name.lower() in c["name"].lower()]

    def list_all(self):
        return self.contacts
