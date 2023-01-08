###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###

import json
from account import Account
from user import User
from libraryDatabase import LibraryDatabase
from book import Book


class Liberian(User):
    """
    Librarian class to represent a librarian in the library
    This class inherits from the User class
    """

    b_limit = 10

    def __init__(self, f_name, l_name, department='library', account=None):
        super().__init__(f_name, l_name, account)
        self.department = department

    def menu(self):
        """
        Prints the menu for the librarian
        """
        print("\n", "*"*50, sep="")
        print(
            f"""Welcome {self.f_name} {self.l_name} to the menu for 'Liberian'""")
        while True:
            print(f"""
Choose an option:
1.  Search for a book
2.  Check lost books
3.  Check reserved books
4.  Check borrowed books
5.  Check overdue books
6.  Check fines
7.  View account details
8.  Add a book
9.  Remove a book
10. Update a book
11. Add a user
12. Remove a user
13. Update a user
q.  Logout
""")
            choice = input("\nSelect Option (1-13|q): ")
            switcher = {
                "1": self.search_book,
                "2": self.check_lost_books,
                "3": self.check_reserved_books,
                "4": self.check_borrowed_books,
                "5": self.check_overdue_books,
                "6": self.check_fines,
                "7": self.view_account_details,
                "8": self.add_book,
                "9": self.remove_book,
                "10": self.update_book,
                "11": self.add_user,
                "12": self.remove_user,
                "13": self.update_user,
                "q": self.logout
            }.get(choice, "Invalid choice")

            try:
                if switcher != "Invalid choice":
                    perform = switcher()
                    if perform == "logout":
                        return

                    input("\nPress Enter to continue...")

                else:
                    print("Invalid choice")
                    print("Try again...")

            except KeyboardInterrupt:
                print("\nProgram terminated by user")
                break

            except Exception as e:
                print(e)

    @staticmethod
    def check_lost_books():
        """ 
        Checks the lost books and prints them out
        """

        print("Checking lost books...")
        print("Lost books:")
        print(f"S/N".ljust(10), f"ISBN".ljust(20), f"Title".ljust(30),
              f"User Id".ljust(15), f"User Name".ljust(20), f"Lost Date ".ljust(20))

        with open("accounts.json") as fd:
            acc = json.load(fd)

            userTypes = ["student", "staff", "librarian"]
            index = 1
            # loop through the accounts student , staff and librarian
            for userType in userTypes:
                for user in acc[userType]:
                    for book in acc[userType][user]["l_lost_books"]:
                        getBook = LibraryDatabase.getBook(book['isbn'])[0]
                        currentBook = Book(*getBook)
                        if currentBook:
                            userName = User.ellipsisWord(
                                acc[userType][user]["f_name"] + " " + acc[userType][user]["l_name"], 18)
                            title = User.ellipsisWord(currentBook.title)
                            print(f"{index}".ljust(10), f"{currentBook.isbn}".ljust(20), f"{title}".ljust(30),
                                  f"{user}".ljust(15),  f"{userName}".ljust(20), f"{book['date_lost']}".ljust(20))
                            index += 1

    def check_reserved_books(self):
        """ 
        Checks the reserved books and prints them out
        """

        print("Checking reserved books...")
        print("Reserved books:")
        print(f"S/N".ljust(10), f"ISBN".ljust(20), f"Title".ljust(30),
              f"User Id".ljust(15), f"User Name".ljust(20), f"Reserved Date ".ljust(20))

        with open("accounts.json") as fd:
            acc = json.load(fd)

            userTypes = ["student", "staff", "librarian"]
            index = 1
            # loop through the accounts student , staff and librarian
            for userType in userTypes:
                for user in acc[userType]:
                    for book in acc[userType][user]["l_books_reserved"]:
                        getBook = LibraryDatabase.getBook(book['isbn'])[0]
                        currentBook = Book(*getBook)
                        if currentBook:
                            userName = User.ellipsisWord(
                                acc[userType][user]["f_name"] + " " + acc[userType][user]["l_name"], 18)
                            title = User.ellipsisWord(currentBook.title)
                            print(f"{index}".ljust(10), f"{currentBook.isbn}".ljust(20), f"{title}".ljust(30),
                                  f"{user}".ljust(15),  f"{userName}".ljust(20), f"{book['date_reserved']}".ljust(20))
                            index += 1

    def check_borrowed_books(self):
        """
        Checks the borrowed books and prints them out
        """
        
        print("Checking borrowed books...")
        print("Borrowed books:")
        print(f"S/N".ljust(10), f"ISBN".ljust(20), f"Title".ljust(30),
              f"User Id".ljust(15), f"User Name".ljust(20), f"Borrowed Date ".ljust(20))

        with open("accounts.json") as fd:
            acc = json.load(fd)

            userTypes = ["student", "staff", "librarian"]
            index = 1
            # loop through the accounts student , staff and librarian
            for userType in userTypes:
                for user in acc[userType]:
                    for book in acc[userType][user]["l_books_borrowed"]:
                        getBook = LibraryDatabase.getBook(book['isbn'])[0]
                        currentBook = Book(*getBook)
                        if currentBook:
                            userName = User.ellipsisWord(
                                acc[userType][user]["f_name"] + " " + acc[userType][user]["l_name"], 18)
                            title = User.ellipsisWord(currentBook.title)
                            print(f"{index}".ljust(10), f"{currentBook.isbn}".ljust(20), f"{title}".ljust(30),
                                  f"{user}".ljust(15),  f"{userName}".ljust(20), f"{book['date_borrowed']}".ljust(20))
                            index += 1

    def check_returned_books(self):
        """
        Checks the returned books and prints them out
        """

        print("Checking returned books...")
        print("Returned books:")
        print(f"S/N".ljust(10), f"ISBN".ljust(20), f"Title".ljust(30),
              f"User Id".ljust(15), f"User Name".ljust(20), f"Returned Date ".ljust(20))

        with open("accounts.json") as fd:
            acc = json.load(fd)

            userTypes = ["student", "staff", "librarian"]
            index = 1
            # loop through the accounts student , staff and librarian
            for userType in userTypes:
                for user in acc[userType]:
                    for book in acc[userType][user]["l_books_returned"]:
                        getBook = LibraryDatabase.getBook(book['isbn'])[0]
                        currentBook = Book(*getBook)
                        if currentBook:
                            userName = User.ellipsisWord(
                                acc[userType][user]["f_name"] + " " + acc[userType][user]["l_name"], 18)
                            title = User.ellipsisWord(currentBook.title)
                            print(f"{index}".ljust(10), f"{currentBook.isbn}".ljust(20), f"{title}".ljust(30),
                                  f"{user}".ljust(15),  f"{userName}".ljust(20), f"{book['date_returned']}".ljust(20))
                            index += 1

    def check_overdue_books(self):
        """
        Checks the overdue books and prints them out
        """

        print("Checking overdue books...")
        print("Overdue books:")
        print(f"S/N".ljust(10), f"ISBN".ljust(20), f"Title".ljust(30),
              f"User Id".ljust(15), f"User Name".ljust(15), f"Overdue Date ".ljust(22), f"Overdue Days ".ljust(15), f"Fine".ljust(10))

        with open("accounts.json") as fd:
            acc = json.load(fd)

            userTypes = ["student", "staff", "librarian"]
            index = 1
            # loop through the accounts student , staff and librarian
            for userType in userTypes:
                for user in acc[userType]:
                    for book in acc[userType][user]["l_books_borrowed"]:
                        getBook = LibraryDatabase.getBook(book['isbn'])[0]
                        currentBook = Book(*getBook)
                        if currentBook:
                            userName = User.ellipsisWord(
                                acc[userType][user]["f_name"] + " " + acc[userType][user]["l_name"], 10)
                            account = Account(
                                acc[userType][user]["id"],
                                acc[userType][user]["password"],
                                acc[userType][user]["f_name"],
                                acc[userType][user]["l_name"],
                                acc[userType][user]["l_books_borrowed"],
                                acc[userType][user]["l_books_reserved"],
                                acc[userType][user]["l_return_books"],
                                acc[userType][user]['l_lost_books'],
                                acc[userType][user]["acc_fine"],
                                userType
                            )
                            title = User.ellipsisWord(currentBook.title)
                            overdueDays = account.get_days_overlap(
                                book['date_borrowed'])
                            if overdueDays > 0:
                                fine = account.get_late_fine(
                                    book['date_borrowed'])
                                print(f"{index}".ljust(10), f"{currentBook.isbn}".ljust(20), f"{title}".ljust(30),
                                      f"{user}".ljust(15),  f"{userName}".ljust(15), f"{book['date_borrowed']}".ljust(22), f"{overdueDays} days".ljust(15), f"£ {fine}".ljust(10))
                                index += 1

    def check_fines(self):
        """
        Checks the fines and prints them out
        """
        
        print("Checking fines...")
        print("Fines:")
        print(f"S/N".ljust(10), f"User Id".ljust(15),
              f"User Name".ljust(15), f"Fine".ljust(10))

        with open("accounts.json") as fd:
            acc = json.load(fd)

            userTypes = ["student", "staff", "librarian"]
            index = 1
            # loop through the accounts student , staff and librarian
            for userType in userTypes:
                for user in acc[userType]:
                    if acc[userType][user]["acc_fine"] is not None and acc[userType][user]["acc_fine"] > 0:
                        userName = User.ellipsisWord(
                            acc[userType][user]["f_name"] + " " + acc[userType][user]["l_name"], 10)
                        print(f"{index}".ljust(10), f"{user}".ljust(15),  f"{userName}".ljust(
                            15), f"£ {acc[userType][user]['acc_fine']}".ljust(10))
                        index += 1

    def add_book(self):
        """ 
        Adds a book to the library database
        """

        print("Adding a book...")
        try:
            title = input("Enter the title of the book: ")
            authors = input("Enter the authors of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            publisher = input("Enter the publisher of the book: ")
            publication_date = input(
                "Enter the publication date of the book: ")
            copies = int(input("Enter the number of copies of the book: "))

            # check if book exists
            print("Checking if book exists...")
            if len(LibraryDatabase.getBook(isbn)) > 0:
                print(
                    "Book already exists in the library database and cannot be added again")
                return

            book = Book(isbn, title, authors, isbn,
                        publisher, publication_date, copies)
            if LibraryDatabase.insertBook(book):
                print("Book added successfully")

        except ValueError:
            print("Invalid number of copies")

        except Exception as e:
            print("Error adding book: ", e)

    def remove_book(self):
        """ 
        Removes a book from the library database
        """

        print("Removing a book...")
        isbn = input("Enter the ISBN of the book: ")
        LibraryDatabase.deleteBook(isbn)

    def update_book(self):
        """ 
        Updates a book in the library database
        """

        print("Updating a book...")
        isbn = input("Enter the ISBN of the book: ")
        # check if book exists
        if not LibraryDatabase.check_book(isbn):
            print("Book does not exist")
            return

        title = input("Enter the title of the book: ")
        authors = input("Enter the authors of the book: ")
        publisher = input("Enter the publisher of the book: ")
        publication_date = input("Enter the publication date of the book: ")
        copies = input("Enter the number of copies of the book: ")

        book = Book(title, authors, isbn, publisher, publication_date, copies)
        LibraryDatabase.updateBook(book)

    def add_user(self):
        """
        Adds a user to the library Account
        """

        print("Adding a user...")
        try:
            a_id = int(input("Enter your id: "))
            f_name = input("Enter your first name: ")
            l_name = input("Enter your last name: ")
            password = input("Enter your password: ")
            userTypeEnum = ["student", "staff", "librarian"]

            userType = input(
                "Enter your user type (student|staff|librarian): ")

            if userType not in userTypeEnum:
                print("Invalid user type")
                return

            class_or_department = input("Enter your class or department: ")

            account = Account.create_account(
                a_id, password, f_name, l_name, userType, class_or_department)

            if account:
                print("Account created successfully")
                self.menu()
            else:
                print("Account creation failed account already exist with the same id")
                input("\nPress Enter to continue...")
                self.menu()
                return

        except KeyboardInterrupt:
            print("\nProgram terminated by user")

        except ValueError:
            print("Id must be an integer value try again ...")
            self.add_user()

        except Exception as e:
            print("Error: ", e)
            self.menu()

    def remove_user(self):
        """ 
        Removes a user from the library Account
        """

        print("Removing a user...")
        a_id = input(
            "Enter your User ID (Note that your User ID should be in this format: student888): ")

        if (a_id == f'{self.account.userType}{self.account.a_id}'):
            print("You cannot remove yourself")
            input("\nPress Enter to continue...")
            return

        removed = Account.remove_account(a_id)
        if removed:
            print("User removed successfully")
            input("\nEnter any key to continue...")

        else:
            print("User does not exist")
            input("\nEnter any key to continue...")

    def update_user(self):
        pass

    def __repr__(self):
        """
        Returns the string representation of the object
        """
        return f"Liberian({self.f_name}, {self.l_name}, {self.department}, {self.account})"

# %%
