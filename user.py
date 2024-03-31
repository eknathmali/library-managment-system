from typing import Dict

class User:
    def __init__(self, name: str, user_id: str):
        """Initialization of User object with a name and user ID."""
        self.name = name
        self.user_id = user_id

    def to_dict(self) -> Dict:
        """Convert the User object to a dictionary."""
        return {
            "name": self.name,
            "user_id": self.user_id
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Create a User object from a dictionary."""
        return cls(data["name"], data["user_id"])

    def __str__(self):
        """Return a string representation of the User."""
        return f"{self.name} (User ID: {self.user_id})"
