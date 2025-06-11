class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def check_out(self):
        if self._is_checked_out:
            raise Exception(f"The book '{self.title}' is already checked out.")
        self._is_checked_out = True
    
    def return_book(self):
        if not self._is_checked_out:
            raise Exception(f"The book '{self.title}' is not checkoud out.")
        self._is_checked_out = False
    def is_available(self):
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You have checked out '{book.title}' by {book.author}.")
                return
        print(f"Sorry, '{title}' is not available for checkout.")
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"You have returned '{book.title}' by {book.author}.")
                return
        print(f"Sorry, '{title}' was not checked out or does not exist in the library.")
        
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
