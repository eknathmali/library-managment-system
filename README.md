# Library Management System

This is a simple command-line Library Management System that allows users to manage books, users, check out and check in books, and track book availability.

## Usage

### Adding a Book

- **Function**: add_book
- **Command**: `python main.py add-book "Book Title" "Book Author" "ISBN Number"`
- **Purpose**: Add a new book to the library.
- **Example**: `python main.py add-book "Life of SPY" "Eknath Mali" "9780306406157"`

* Note: ISBN number should be of length 13
### Listing Books

- **Function**: list_books
- **Command**: `python main.py list-books`
- **Purpose**: List all the books available in the library.
- **Example**: `python main.py list-books`

### Adding a User

- **Function**: add_user
- **Command**: `python main.py add-user "User Name" "User ID"`
- **Purpose**: Add a new user to the library.
- **Example**: `python main.py add-user "Rajesh" "1236"`

* Note: No duplicate ID's allowed

### Listing Users

- **Function**: list_users
- **Command**: `python main.py list-users`
- **Purpose**: List all the users registered in the library.
- **Example**: `python main.py list-users`

### Checking Out a Book

- **Function**: checkout_
- **Command**: `python main.py checkout- "User ID" "ISBN Number"`
- **Purpose**: Check out a book for a user.
- **Example**: `python main.py checkout- "1236" "9780306406157"`

Note: IF book is already used by other user then will get error as `Other user already checked out the book..(not aavaiable to use)`

### Checking In a Book

- **Function**: checkin_
- **Command**: `python main.py checkin- "User ID" "ISBN Number"`
- **Purpose**: Check in a book that was previously checked out by a user.
- **Example**: `python main.py checkin- "1236" "9780306406157"`
Note: If checkedin books is being tried to checkin again then will get error as `Book is already checked in (Avaiable to use)`

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. List all available commands
    ```bash
    python main.py --help
    ```
* Note: You can always use --help to see the required arguments for each function.

