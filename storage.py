import json
from typing import List, Type
from book import Book
from user import User

class Storage:
    def __init__(self, filename: str):
        """Initialize the Storage with a filename."""
        self.filename = filename
        self.data = self.load_data()

    def load_data(self) -> List[Type]:
        """Load data from the file and deserialize into objects."""
        try:
            with open(self.filename, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    # Handle empty file
                    return []
                return [self.deserialize(item) for item in data]
        except FileNotFoundError:
            # Create an empty file if it doesn't exist
            with open(self.filename, 'w') as file:
                file.write("[]")
            return []

    def save_data(self):
        """Save data to the file by serializing objects."""
        with open(self.filename, 'w') as file:
            json.dump([item.__dict__ for item in self.data], file, indent=4)

    def deserialize(self, data: dict) -> Type:
        """Deserialize data into either a Book or User object."""
        # Assuming data is either Book or User data
        if "title" in data:
            return Book(data["title"], data["author"], data["isbn"], data["available"])
        elif "name" in data:
            return User(data["name"], data["user_id"])

        raise ValueError("Invalid data format")
