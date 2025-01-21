class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"The book '{title}' has been checked out."
                return f"The book '{title}' is already checked out."
        return f"The book '{title}' is not in the library."

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"The book '{title}' has been returned."
                return f"The book '{title}' was not checked out."
        return f"The book '{title}' is not in the library."

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        return available_books
