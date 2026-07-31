class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [b for b in self.books if b.author.lower() == author.lower()]

    def list_books(self):
        for b in self.books:
            print(f"'{b.title}' by {b.author} ({b.year})")
