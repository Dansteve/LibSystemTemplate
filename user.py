###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###

import datetime
from book import Book

from libraryDatabase import LibraryDatabase


class User:
    """
    User class to represent a user of the library management system
    """

    # USER CONSTANTS
    __MAX_BORROW_LIMIT = 5
    __MAX_LOAN_PERIOD = 14
    __MAX_RESERVE_LIMIT = 3
    __MAX_RESERVATION_PERIOD = 21


    def __init__(self, f_name, l_name, account=None):
        self.f_name = f_name
        self.l_name = l_name
        self.account = account

    def set_limit(self, max_borrow_limit, max_loan_period, max_reserve_limit, max_reservation_period):
        """ 
        Set the limit for the user.\n
        The user can set the limit for the number of books they can borrow, the number of books they can reserve, the maximum loan period, and the maximum reservation period.\n
        """

        self.__MAX_BORROW_LIMIT = max_borrow_limit
        self.__MAX_LOAN_PERIOD = max_loan_period
        self.__MAX_RESERVE_LIMIT = max_reserve_limit
        self.__MAX_RESERVATION_PERIOD = max_reservation_period

    def search_book(self):
        """ 
        Search for a book.\n
        The user can search for a book by title, author, or ISBN.\n
        If the user inputs an invalid choice, they will be asked to make a new selection.\n
        If an exception occurs, it will be caught and the menu will be displayed again.\n
        """
        
        print("Searching for a book...")
        try:
            book_name = input(
                "Enter the title | author | category | publication year | ISBN of the book: ")
            books = LibraryDatabase.search(book_name)

            if len(books) == 0:
                print("No results found")
            else:
                print("Results found: ")
                print(f"S/N".ljust(10), f"Title".ljust(30), f"Author".ljust(30), f"ISBN".ljust(20),
                      f"Publisher".ljust(30), f"Publication Date".ljust(20), f"Copies".ljust(10))
                for sn, b in enumerate(books, 1):
                    book = Book(*b)
                    print(f"{sn}".ljust(10), f"{self.ellipsisWord(book.title)}".ljust(30), f"{self.ellipsisWord(book.authors)}".ljust(30), f"{book.isbn}".ljust(
                        20), f"{self.ellipsisWord(book.publisher)}".ljust(30), f"{book.publication_date}".ljust(20), f"{book.available}".ljust(10))

        except Exception as e:
            print("Error: ", e)

    def borrow_book(self):  
        """ 
        Borrow a book.\n

        The user can borrow a book by title, author, or ISBN.\n
        If the user inputs an invalid choice, they will be asked to make a new selection.\n
        If an exception occurs, it will be caught and the menu will be displayed again.\n
        
        """
        print("Borrowing a book...")
        try:
            book_name = input("Enter the title | author | ISBN of the book: ")
            books = LibraryDatabase.search(book_name)

            if len(books) == 0:
                print("No results found")
            else:
                print("Results found: ")
                print(f"S/N".ljust(10), f"Title".ljust(30), f"Author".ljust(30), f"ISBN".ljust(20),
                      f"Publisher".ljust(30), f"Publication Date".ljust(20), f"Copies".ljust(10))
                for sn, b in enumerate(books, 1):
                    book = Book(*b)
                    print(f"{sn}".ljust(10), f"{self.ellipsisWord(book.title)}".ljust(30), f"{self.ellipsisWord(book.authors)}".ljust(30), f"{book.isbn}".ljust(
                        20), f"{self.ellipsisWord(book.publisher)}".ljust(30), f"{book.publication_date}".ljust(20), f"{book.available}".ljust(10))

                choice = int(input("Enter S/N of the book to borrow: "))
                book = Book(*books[choice-1])
                if book.available > 0:
                    if len(self.account.l_books_borrowed) < self.__MAX_BORROW_LIMIT:
                        # check if the book has been borrowed before by the user {isbn, date_borrowed}
                        if book.isbn in [b['isbn'] for b in self.account.l_books_borrowed]:
                            print("You have already borrowed this book")
                            return

                        self.account.l_books_borrowed.append(
                            {"isbn": book.isbn, "date_borrowed": self.get_date()})
                        book.available -= 1
                        LibraryDatabase.updateBook(book)

                        # check if the book has been reserved by the user and remove it from the list
                        # if book.isbn in [b['isbn'] for b in self.account.l_books_reserved]:
                        self.account.l_books_reserved = [b for b in self.account.l_books_reserved if b['isbn'] != book.isbn]
                        self.account.update_account_json()
                        print("Book borrowed successfully")
                    else:
                        print(f"You have reached your borrowing limit of {self.__MAX_BORROW_LIMIT} books")
                else:
                    print("Book not available")
                    
        except ValueError:
            print("Invalid choice ->", "S/N must be a number")

        except IndexError:
            print("Invalid choice ->", "Kindly select S/N from the list")

        except Exception as e:
            print("Error: ", e)

    def cancel_reservation(self):
        """
        Cancel a reservation.\n
        The user can cancel a reservation by title, author, or ISBN.\n
        If the user inputs an invalid choice, they will be asked to make a new selection.\n
        If an exception occurs, it will be caught and the menu will be displayed again.\n
        """
        
        print("Cancelling reservation...")
        try:
            # show the list of reserved books
            if len(self.account.l_books_reserved) == 0:
                print("You have not reserved any book")
                return

            print("Reserved books: ")
            print(f"S/N".ljust(10), f"Title".ljust(30), f"Author".ljust(30), f"ISBN".ljust(20),
                    f"Date Reserved".ljust(20))

            for sn, b in enumerate(self.account.l_books_reserved, 1):
                getBook = LibraryDatabase.getBook(b['isbn'])[0]
                book = Book(*getBook)
                print(f"{sn}".ljust(10), f"{self.ellipsisWord(book.title)}".ljust(30), f"{self.ellipsisWord(book.authors)}".ljust(30), f"{book.isbn}".ljust(
                        20), f"{b['date_reserved']}".ljust(20))

            choice = int(input("Enter S/N of the book to cancel reservation: "))
            book = Book(*LibraryDatabase.getBook(self.account.l_books_reserved[choice-1]['isbn'])[0])
            self.account.l_books_reserved = [b for b in self.account.l_books_reserved if b['isbn'] != book.isbn]
            self.account.update_account_json()
            print("Reservation cancelled successfully")
            
            
        except Exception as e:
            print("Error: ", e)

    def view_borrowed_books(self):
        """ 
        View borrowed books.\n
        The user can view all the books they have borrowed.\n
        If the user has not borrowed any book, they will be notified.\n
        If an exception occurs, it will be caught and the menu will be displayed again.\n
        """

        print("Borrowed books: ")
        print(f"S/N".ljust(10), f"Title".ljust(30), f"Author".ljust(30), f"ISBN".ljust(20),
              f"Date Borrowed".ljust(20), f"Date Due".ljust(20))

        for sn, b in enumerate(self.account.l_books_borrowed, 1):
            getBook = LibraryDatabase.getBook(b['isbn'])[0]
            book = Book(*getBook)
            print(f"{sn}".ljust(10), f"{self.ellipsisWord(book.title)}".ljust(30), f"{self.ellipsisWord(book.authors)}".ljust(30), f"{book.isbn}".ljust(
                20), f"{b['date_borrowed']}".ljust(20), f"{self.get_due_date(b['date_borrowed'])}".ljust(20))

    def reserve_book(self):
        """ 
        Reserve a book.\n
        
        The user can reserve a book by title, author, or ISBN.\n
        If the user inputs an invalid choice, they will be asked to make a new selection.\n
        If an exception occurs, it will be caught and the menu will be displayed again.\n
        """

        print("Reserving a book...")
        try:
            book_name = input("Enter the title | author | ISBN of the book: ")
            books = LibraryDatabase.search(book_name)

            if len(books) == 0:
                print("No results found")
            else:
                print("Results found: ")
                print(f"S/N".ljust(10), f"Title".ljust(30), f"Author".ljust(30), f"ISBN".ljust(20),
                      f"Publisher".ljust(30), f"Publication Date".ljust(20), f"Copies".ljust(10))
                for sn, b in enumerate(books, 1):
                    book = Book(*b)
                    print(f"{sn}".ljust(10), f"{self.ellipsisWord(book.title)}".ljust(30), f"{self.ellipsisWord(book.authors)}".ljust(30), f"{book.isbn}".ljust(
                        20), f"{self.ellipsisWord(book.publisher)}".ljust(30), f"{book.publication_date}".ljust(20), f"{book.available}".ljust(10))

                choice = int(input("Enter S/N of the book to reserve: "))
                book = Book(*books[choice-1])

                # check if the book has been borrowed before by the user {isbn, date_borrowed}
                if book.isbn in [b['isbn'] for b in self.account.l_books_borrowed]:
                    print("You have already borrowed this book")
                    return

                # check if the book has been reserved by the user
                if book.isbn in [b['isbn'] for b in self.account.l_books_reserved]:
                    print("You have already reserved this book")
                    return

                if len(self.account.l_books_borrowed) >= self.__MAX_RESERVE_LIMIT:
                    print(f"You have reached your reservation limit of {self.__MAX_RESERVE_LIMIT} books ")
                    return

                if book.available > 0:
                    print("Book is available, you can borrow it")
                else:

                    if len(self.account.l_books_borrowed) < self.__MAX_RESERVE_LIMIT:
                        self.account.l_books_reserved.append(
                            {"isbn": book.isbn, "date_reserved": self.get_date()})
                        self.account.update_account_json()
                        print("Book reserved successfully")

        except ValueError:
            print("Invalid choice ->", "S/N must be a number")

        except IndexError:
            print("Invalid choice ->", "Kindly select S/N from the list")

        except Exception as e:
            print("Error: ", e)

    def view_reserved_books(self):
        """ 
        View reserved books.\n
        The user can view all the books they have reserved.\n
        If the user has not reserved any book, they will be notified.\n
        """

        print("Reserved books: ")
        print(f"S/N".ljust(10), f"Title".ljust(30), f"Author".ljust(30), f"ISBN".ljust(20),
              f"Date Reserved".ljust(20), f"Expiration Date ".ljust(20))

        for sn, b in enumerate(self.account.l_books_reserved, 1):
            getBook = LibraryDatabase.getBook(b['isbn'])[0]
            book = Book(*getBook)
            print(f"{sn}".ljust(10), f"{self.ellipsisWord(book.title)}".ljust(30), f"{self.ellipsisWord(book.authors)}".ljust(30), f"{book.isbn}".ljust(
                20), f"{b['date_reserved']}".ljust(20), f"{self.get_reservation_expiry_date(b['date_reserved'])}".ljust(20))

    def return_book(self):
        """ 
        Return a book.\n
        The user can return a book they have borrowed.\n
        If the user has not borrowed any book, they will be notified.\n
        """

        print("Returning a book...")
        if(len(self.account.l_books_borrowed) == 0):
            print("You have no borrowed books")
            return

        # show borrowed books and ask for the book to be returned
        self.view_borrowed_books()

        try:
            choice = int(input("Enter S/N of the book to return: "))
            book = Book(
                *LibraryDatabase.getBook(self.account.l_books_borrowed[choice-1]['isbn'])[0])
            self.account.l_books_borrowed.pop(choice-1)
            book.available += 1
            LibraryDatabase.updateBook(book)

            # update history of returned books and date returned
            self.account.l_return_books.append({"isbn": book.isbn, "date_returned": self.get_date()})
            self.account.update_account_json()
            print("Book returned successfully")

        except ValueError:
            print("Invalid choice ->", "S/N must be a number")
                                
        except IndexError:
            print("Invalid choice ->", "Kindly select S/N from the list")

        except Exception as e:
            print("Error: ", e)

    def make_a_book_as_lost(self):
        """ 
        Make a book as lost.\n   
        The user can make a book they have borrowed as lost.\n
        If the user has not borrowed any book, they will be notified.\n
        """

        print("Making a book as lost...")
        # show borrowed books and ask for the book to make as lost
        self.view_borrowed_books()
        try:
            choice = int(input("Enter S/N of the book to make as lost: "))
            book = Book(
                *LibraryDatabase.getBook(self.account.l_books_borrowed[choice-1]['isbn'])[0])
            self.account.l_books_borrowed.pop(choice-1)

            # update history of lost books and date lost
            self.account.l_lost_books.append({"isbn": book.isbn, "date_lost": self.get_date(), 'has_paid': False})
            self.account.update_account_json()
            print("Book marked as lost successfully")

        except ValueError:
            print("Invalid choice ->", "S/N must be a number")
                    
        except IndexError:
            print("Invalid choice ->", "Kindly select a S/N from the list of books borrowed")

        except Exception as e:
            print("Error: ", e)

    def view_lost_books(self):
        """
        View lost books.\n
        The user can view all the books they have marked as lost.\n
        If the user has not marked any book as lost, they will be notified.\n
        """ 
    
        print("Lost books: ")
        print(f"S/N".ljust(10), f"Title".ljust(30), f"Author".ljust(30), f"ISBN".ljust(20),
                f"Date Lost".ljust(20))

        for sn, b in enumerate(self.account.l_lost_books, 1):
            getBook = LibraryDatabase.getBook(b['isbn'])[0]
            book = Book(*getBook)
            print(f"{sn}".ljust(10), f"{self.ellipsisWord(book.title)}".ljust(30), f"{self.ellipsisWord(book.authors)}".ljust(30), f"{book.isbn}".ljust(
                20), f"{b['date_lost']}".ljust(20))

                
    def view_account_details(self):
        """ 
        View account details.\n
        The user can view their account details.\n
        """

        print("Account Details", self.account)

    def pay_fine(self):
        """
        Pay the current account fine.

        Parameters:
            None

        Returns:
            None

        """

        self.acc_fine = 0
        self.account.update_account_json()

    def logout(self):
        """ 
        Logout.\n
        """

        print("Logging out...")
        return 'logout'

    def get_date(self):
        """
        Get current date.\n
        """ 

        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_due_date(self, date):
        """ 
        Get due date.\n

        Parameters:
        ----------
        date: str
            Date to get due date from.\n

        Returns:
        -------
        str
            Due date.\n

        """

        return self.get_date_after(date, self.__MAX_LOAN_PERIOD)

    def get_reservation_expiry_date(self, date):
        """
        Get reservation expiry date.

        Parameters:
        ----------
        date: str
            Date to get reservation expiry date from.

        Returns:
        -------
        str
            Reservation expiry date.\n


        """
        return self.get_date_after(date, self.__MAX_RESERVATION_PERIOD);
    
    def extend_due_date(self, date):
        """ 
        Extend due date.
        
        Parameters:
        ----------
        date: str
            Date to extend due date from.

        Returns:
        -------
        str
            Extended due date.


        """ 

        return self.get_date_after(date, 2)

    def extend_reservation(self, date):
        """ 
        Extend reservation.
        
        Parameters:
        ----------
        date: str
            Date to extend reservation from.

        Returns:
        -------
        str
            Extended reservation.
            
        """

        return self.get_date_after(date, 5)

    @staticmethod
    def ellipsisWord(word, length=25):
        """
        Ellipsis word

        Parameters:
        ----------
        word: str
            Word to ellipsis.
        length: int
            Length of word to ellipsis.

        Returns:
        -------
        str
            Ellipsis word.

        """

        return word if len(word) <= length else word[0:length - 3] + '...'

    @staticmethod
    def get_date_after(date, days):
        """ 
        Get date after a number of days.
        
        Parameters:
        ----------
        date: str
            Date to get date after from.
        days: int
            Number of days to add to date.
            
        Returns:
        -------
        str
            Date after a number of days.
        
        """

        try:
            date = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S")
            return (date + datetime.timedelta(days=days)).strftime("%d/%m/%Y %H:%M:%S")
        except Exception as e:
            print("Error: ", e)
            return None

    def __rpr__(self):
        """ 
        Return a string representation of the object.
        """
        
        return f"""{self.f_name} {self.l_name},{self.account}"""
