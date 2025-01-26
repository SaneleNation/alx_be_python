# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # file size in MB

    def __str__(self):
        return f"{super().__str__()} [EBook: {self.title} by {self.author}, File Size: {self.file_size}KB]"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} [PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}]"


# Composition - Library
class Library:
    def __init__(self):
        self.books = []  # List to store book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book, EBook, or PrintBook can be added to the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")
