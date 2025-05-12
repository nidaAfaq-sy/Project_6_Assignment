class Book:
    # Class variable to track total number of books
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment the count each time a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books


# Example usage:
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print("Total books:", Book.get_total_books())
