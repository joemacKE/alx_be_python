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
        self.available = 1
    
class Library(Book):
    def add_book(self, available):
        self.available += self.author

    def check_out_book(self, title):
        if self._is_checked_out:
            self.title -= self.title
    def return_book(self, title, available):
        self.available += self.title
        
    def list_available_books(self):
        print(f"Available books after setup: {self.title} by {self.author}")