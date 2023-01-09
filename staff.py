###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: 
###

from user import User

class Staff(User):
    """
    Staff class to represent a staff member in the library
    This class inherits from the User class
    """

    # USER CONSTANTS
    __MAX_BORROW_LIMIT = 5
    __MAX_LOAN_PERIOD = 7
    __MAX_RESERVE_LIMIT = 3
    __MAX_RESERVATION_PERIOD = 21

    def __init__(self, f_name, l_name, department, account=None):
        super().__init__(f_name, l_name, account)
        self.department = department
        super().set_limit(self.__MAX_BORROW_LIMIT, self.__MAX_LOAN_PERIOD,
                          self.__MAX_RESERVE_LIMIT, self.__MAX_RESERVATION_PERIOD)

    def menu(self):
        """ 
        Display the menu for the Staff.\n
        The user can choose to search for a book, borrow a book, reserve a book, return a book, view borrowed books, view reserved books, make a book lost, view lost books, view account details, or logout.\n
        If the user inputs an invalid choice, they will be asked to make a new selection.\n
        If an exception occurs, it will be caught and the menu will be displayed again.\n
        """

        print("\n", "*"*50, sep="")
        print(f"""Welcome {self.f_name} {self.l_name} to the menu for 'Staff'""")
        while True:
            print(f"""
Choose an option:
1.  Search for a book
2.  Borrow a book
3.  Reserve a book
4.  Return a book
5.  Renew a borrowed book
6.  View borrowed books
7.  View reserved books
8.  Cancel a reservation
9.  Mark a book lost
10. View Lost books
11. Pay fine
12. View account details
q. Logout
""")
            choice = input("\nSelect Option (1-12|q): ")
            switcher = {
                "1": self.search_book,
                "2": self.borrow_book,
                "3": self.reserve_book,
                "4": self.return_book,
                "5": self.renew_borrowed_book,
                "6": self.view_borrowed_books,
                "7": self.view_reserved_books,
                "8": self.cancel_reservation,
                "9": self.make_a_book_as_lost,
                "10": self.view_lost_books,
                "11": self.pay_fine,
                "12": self.view_account_details,
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
            
            
    def __repr__(self):
        """ 
        Return a string representation of the Staff.\n
        """
        
        return f"Staff({self.f_name}, {self.l_name}, {self.department}, {self.account})"
