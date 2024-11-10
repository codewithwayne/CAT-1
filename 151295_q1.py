class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}' by {book.author}.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books and book.mark_as_returned():
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"Error: '{book.title}' is not in the borrowed books list.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")


def main():
    
    book1 = Book("Perfecting lives", "JICA")
    book2 = Book("Diary of a wimpy kid", "Idek")
    book3 = Book("Highschool set books", "844 is tedious")
    book4 = Book("Life of Wayne - The autobiography", "Wayne Imbuga")
    all_books = [book1, book2, book3, book4]  
    
    
    member = LibraryMember("Michael Kors", "15000")

    while True:
        print("\n--- Library System ---")
        print("1. View available books")
        print("2. Borrow a book")
        print("3. View borrowed books")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("\nAvailable books:")
            for book in all_books:
                if not book.is_borrowed:
                    print(f"- {book.title} by {book.author}")
            if all(book.is_borrowed for book in all_books):
                print("No books available at the moment.")

        elif choice == '2':
            print("\nAvailable books to borrow:")
            available_books = [book for book in all_books if not book.is_borrowed]
            if available_books:
                for idx, book in enumerate(available_books):
                    print(f"{idx + 1}. {book.title} by {book.author}")
                book_choice = int(input("Enter the number of the book to borrow: ")) - 1
                if 0 <= book_choice < len(available_books):
                    member.borrow_book(available_books[book_choice])
                else:
                    print("Invalid choice.")
            else:
                print("No books available to borrow.")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            print("\nYour borrowed books:")
            if member.borrowed_books:
                for idx, book in enumerate(member.borrowed_books):
                    print(f"{idx + 1}. {book.title} by {book.author}")
                book_choice = int(input("Enter the number of the book to return: ")) - 1
                if 0 <= book_choice < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[book_choice])
                else:
                    print("Invalid choice.")
            else:
                print("You have no borrowed books to return.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
