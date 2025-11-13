from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    def checkout(self):
        if not self.available:
            print("This book is already checked out.")
            return
        
        self.available = False
        due = datetime.today() + timedelta(weeks=2)
        self.due_date = due.strftime("%Y-%m-%d")
        self.checkouts += 1

        print(f"{self.title} checked out successfully! Due: {self.due_date}")

    def return_book(self):
        if self.available:
            print("This book is already in the library.")
            return
        
        self.available = True
        self.due_date = None
        print(f"{self.title} has been returned. Thank you!")

books = []
for data in library_books:
    book = Book(
        id=data['id'],
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        available=data['available'],
        due_date=data['due_date'],
        checkouts=data['checkouts']
    )
    books.append(book)



# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
def view_available_books(books):
    for book in books:
        if book["available"]:
            print(f"{book['id']} - {book['title']} by {book['author']}")





# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
def search_books(books):
    term = input("Enter a author or genre to search: ").lower()
    for book in books:
        author = book["author"].lower()
        genre = book["genre"].lower()
        if term in author or term in genre:
            print(f"{book['id']} - {book['title']} by {book['author']}")



# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
def checkout(books):
    book_id = input("Enter a book id to checkout: ").upper()
    for book in books:
        if book['id'] == book_id:
            if not book['available']:
                print("This book is already checked out.")
                return
            book['available'] = False
            due = datetime.today() + timedelta(weeks=2)
            book["due_date"] = due.strftime("%Y-%m-%d")
            book["checkouts"] += 1
            print(f"{book['id']} checked out sucessfully! Due date: {book['due_date']}")
            return
    print("Book ID not found.")



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
def return_book(books):
    book_id = input("Enter a book ID to return: ").strip().upper()
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                print("This book is already in the library.")
                return
            book["available"] = True
            book["due_date"] = None
            print(f"{book['title']} has been returned. Thank you!")
            return
    print("Book ID not found.")



# TODO: Create a function to list all overdue books
def overdue_books(books):
    today = datetime.today()
    for book in books:
        if book["available"]:
            continue
        if book["due_date"] is None:
            continue
        due = datetime.strptime(book["due_date"], "%Y-%m-%d")
        if due < today:
          print(f"{book['id']} - {book['title']} is overdue! (Due: {book['due_date']})")



# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
if __name__ == "__main__":
    # You can use this space to test your functions
    while True:
        print("\n--- Library Menu ---\n"
              "1. View available books\n"
              "2. Search by author or genre\n" \
              "3. Checkout a book\n"
              "4. Return a book\n" 
              "5. View overdue books\n"
              "6. Exit"
              )
        
        choice = input("Choose an option: ")

        if choice == "1":
            for b in books:
                if b.available:
                    print(f"{b.id} - {b.title} by {b.author}")

        elif choice == "2":
            term = input ("Search by author or genre: ").lower()
            found = False 
            for b in books:
                if term in b.author.lower() or term in b.genre.lower():
                    print(f"{b.id} - {b.title} by {b.author}")
                    found = True
            if not found:
                print("No matching books found.")

        elif choice == "3":
            book_id = input("Enter book ID to checkout: ").upper()
            for b in books:
                if b.id == book_id:
                    b.checkout()
                    break
            else:
                print("Book not found.")

        elif choice == "4":
            book_id = input("Enter book ID to return: ").upper()
            for b in books:
                if b.id == book_id:
                    b.return_book()
                    break
            else:
                print("Book not found.")

        elif choice == "5":
            today = datetime.today()
            found =  False
            for b in books:
                if not b.available and b.due_date:
                    due = datetime.strptime(b.due_date, "%Y-%m-%d")
                    if due < today:
                        print(f"{b.id} - {b.title} (Due: {b.due_date})")
                        found = True
            if not found:
                print("No overdue books.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")                                    


              


