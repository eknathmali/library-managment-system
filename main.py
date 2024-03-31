import typer
from storage import Storage
from models import Library
from check import Checkout

app = typer.Typer()

book_storage = Storage("books.json")
user_storage = Storage("users.json")
library = Library(book_storage, user_storage)
checkout = Checkout(library)


@app.command()
def add_book(title: str, author: str, isbn: str):
    """Add a new book to the library."""
    library.add_book(title, author, isbn)

@app.command()
def list_books():
    """List all books in the library."""
    library.list_books()

@app.command()
def add_user(name: str, user_id: str):
    """Add a new user to the library."""
    library.add_user(name, user_id)

@app.command()
def list_users():
    """List all users in the library."""
    library.list_users()

@app.command()
def checkout_(user_id: str, isbn: str):
    """Check out a book for a user."""
    checkout.checkout_book(user_id, isbn)
    typer.echo("Book checked out.")

@app.command()
def checkin_(user_id: str, isbn: str):
    """Check in a book that was checked out."""
    checkout.checkin_book(user_id, isbn)
    typer.echo("Book checked in.")

if __name__ == "__main__":
    app()
