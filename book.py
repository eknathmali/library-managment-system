from typing import Dict

class Book:
    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        """Initialization of Book object."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self) -> Dict:
        """Book object to a dictionary."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        """Book object from a dictionary."""
        return cls(data["title"], data["author"], data["isbn"], data["available"])

    def __str__(self):
        """String representation of the Book object."""
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Available: {self.available}"
