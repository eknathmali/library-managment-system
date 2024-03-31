from typing import Optional

from book import Book
from models import Library
from user import User

class Checkout:
    def __init__(self, library: Library):
        """Initialization of Checkout object with a Library instance."""
        self.library = library

    def checkout_book(self, user_id: str, isbn: str):
        """Checkout a book for a user."""
        user = self.find_user(user_id)
        if user is None:
            raise ValueError("User not found")
        book = self.find_book(isbn)
        if book is None:
            raise ValueError("Book not found")
        if not book.available:
            raise ValueError("Other user already checked out the book (not available to use)")
        book.available = False
        self.library.book_storage.save_data()

    def checkin_book(self, user_id: str, isbn: str):
        """Check in a book that was checked out by a user."""
        user = self.find_user(user_id)
        if user is None:
            raise ValueError("User not found")
        book = self.find_book(isbn)
        if book is None:
            raise ValueError("Book not found")
        if book.available:
            raise ValueError("Book is already checked in (available to use)")
        book.available = True
        self.library.book_storage.save_data()

    def find_user(self, user_id: str) -> Optional[User]:
        """Find a user by their user ID."""
        for user in self.library.user_storage.data:
            if user.user_id == user_id:
                return user
        return None

    def find_book(self, isbn: str) -> Optional[Book]:
        """Find a book by its ISBN."""
        for book in self.library.book_storage.data:
            if book.isbn == isbn:
                return book
        return None
