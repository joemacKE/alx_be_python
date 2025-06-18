class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.title = title
        self.author = author
        self.books = []
    
    def __str__(self):
        return f"Library: {self.title} by {self.author}"

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(f"{self.title} by {self.author}, File Size: {self.file_size}")