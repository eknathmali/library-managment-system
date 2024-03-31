from typing import Optional
from book import Book
from storage import Storage
from user import User

class Library:
    def __init__(self, book_storage: Storage, user_storage: Storage):
        """Initialize the Library with book and user storages."""
        self.book_storage = book_storage
        self.user_storage = user_storage

    def add_book(self, title: str, author: str, isbn: str):
        """add a new book to the library."""

           # Check ISBN length
        if len(isbn) != 13:
            print("Invalid ISBN length. ISBN must be 13 characters.")
            return
        
        # Check for duplicate ISBN
        if any(book.isbn == isbn for book in self.book_storage.data):
            print(f"Duplicate ISBN: {isbn}. Book not added.")
            return
        book = Book(title, author, isbn)
        self.book_storage.data.append(book)
        self.book_storage.save_data()
        print("Book added successfully.")

    def list_books(self):
        """List all books in the library."""
        if not self.book_storage.data:
            print("No books available")
        else:
            for book in self.book_storage.data:
                print(book)

    def add_user(self, name: str, user_id: str):
        """Add a new user to the library."""
        # Check for duplicate user_id
        if any(user.user_id == user_id for user in self.user_storage.data):
            print(f"Duplicate User ID: {user_id}. User not added.")
            return
        user = User(name, user_id)
        self.user_storage.data.append(user)
        self.user_storage.save_data()
        print("User added successfully.")

    def list_users(self):
        """List all users in the library."""
        if not self.user_storage.data:
            print("No users available")
        else:
            for user in self.user_storage.data:
                print(user)
