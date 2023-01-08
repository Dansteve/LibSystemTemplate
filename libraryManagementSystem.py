###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: 
###

from librarian import Liberian
from libraryDatabase import LibraryDatabase
from account import Account
from staff import Staff
from student import Student


class LibraryManagementSystem:
    """
    LibraryManagementSystem class to represent the library management system
    """

    def __init__(self):
        LibraryDatabase.loadBooks()
        Account.load_init_all_accounts()
        LibraryManagementSystem.menu()

    @staticmethod
    def menu():
        """
        Display the main menu for the Library Management System.\n
        The user can choose to login, register, get help, or exit the program.\n
        If the user inputs an invalid choice, they will be asked to make a new selection.\n
        If an exception occurs, it will be caught and the menu will be displayed again.\n
        """

        print("Welcome to the Library Management System")
        print("*"*50)
        print("Select an option:")
        print("1. Login")
        print("2. Register")
        print("3. Help")
        print("q. Exit")
        print("*"*50)

        try:
            choice = input("What would like to do today (1-3|q): ")
            switcher = {
                '1': LibraryManagementSystem.login,
                '2': LibraryManagementSystem.register,
                '3': LibraryManagementSystem.help,
                'q': LibraryManagementSystem.exit
            }.get(choice, "Invalid choice")

            if switcher != "Invalid choice":
                switcher()
            else:
                print("Invalid choice")
                LibraryManagementSystem.menu()

        except KeyboardInterrupt:
            print("\nProgram terminated by user")
            LibraryManagementSystem.exit()

        except Exception as e:
            print("Error: ", e)
            LibraryManagementSystem.menu()

    @staticmethod
    def authenticate(uid, password):
        """
        Authenticate a user with the given user id and password.\n
        If the user id and password are valid, return the account object and user type.\n
        If the user id or password is invalid, return None for both the account object and user type.\n
        If an exception occurs, it will be caught and None will be returned for both the account object and user type.\n

        Parameters:
            uid (str): The user id of the user.
            password (str): The password of the user.

        Returns:
            account (Account): The account object of the user.
            userType (str): The user type of the user.

        Raises:
            Exception: If an exception occurs.
        """

        try:
            account, userType = Account.load_account(uid)
            if account:
                if account.password == password:
                    return account, userType
                else:
                    return None, None
        except Exception as e:
            print("Error: ", 'Invalid user id')
            return None, None

    @staticmethod
    def login():
        """
        Login to the Library Management System.\n
        The user will be asked to enter their user id and password.\n
        If the user id and password are valid, the user will be directed to the appropriate menu.\n
        If the user id or password is invalid, the user will be asked to try again.\n
        If the user inputs 'q' or 'Q', they will be directed back to the main menu.\n
        If an exception occurs, it will be caught and the user will be asked to try again.\n

        Parameters:
            None

        Returns:
            None

        Raises:
            Exception: If an exception occurs.
        """

        uid = input("Enter your User ID (Note that your User ID should be in this format: student888): ")

        if(uid == "q"):
            print("back to main menu")
            LibraryManagementSystem.menu()
            return

        password = input("Enter password: ")

        try:
            account, userType =  LibraryManagementSystem.authenticate(uid, password)
            if account:
                if userType == "student":
                 user =   Student(account.f_name, account.l_name, '', account).menu()
                elif userType == "staff":
                 user = Staff(account.f_name, account.l_name, '', account).menu()
                elif userType == "librarian":
                  user = Liberian(account.f_name, account.l_name, '', account).menu()

                print("back to main menu")
                LibraryManagementSystem.menu()

            else:
                print("Login failure..")
                LibraryManagementSystem.login()
                
        except Exception as e:
            print("Error: ", 'Invalid user id')
            LibraryManagementSystem.login()

    @staticmethod
    def register():
        """
        Register a new user to the Library Management System.\n
        The user will be asked to enter their user id, first name, last name, password, user type, and class or department.\n
        If the user id is already in use, the user will be asked to try again.\n
        If the user type is invalid, the user will be asked to try again.\n
        If the user inputs 'q' or 'Q', they will be directed back to the main menu.\n
        If an exception occurs, it will be caught and the user will be asked to try again.\n

        Parameters:
            None

        Returns:
            None

        Raises:
            Exception: If an exception occurs.
        """

        print("Register ...")
        try:
            a_id = int(input("Enter your id: "))
            f_name = input("Enter your first name: ")
            l_name = input("Enter your last name: ")
            password = input("Enter your password: ")
            userTypeEnum = ["student", "staff"]

            userType = input(
                "Enter your user type (student|staff): ")

            if userType not in userTypeEnum:
                print("Invalid user type")
                input("\nPress Enter to continue...")
                LibraryManagementSystem.menu()
                
            class_or_department = input("Enter your class or department: ")
            
            account = Account.create_account(a_id, password, f_name, l_name, userType, class_or_department)

            if account:
                print("Account created successfully")
                LibraryManagementSystem.menu()
            else:
                print("Account creation failed account already exist with the same id")
                input("\nPress Enter to continue...")
                LibraryManagementSystem.menu()
                return
                

        except KeyboardInterrupt:
            print("\nProgram terminated by user")
            LibraryManagementSystem.exit()

        except ValueError:
            print("Id must be an integer value try again ...")
            LibraryManagementSystem.register()

        except Exception as e:
            print("Error: ", e)
            LibraryManagementSystem.menu()

    @staticmethod
    def help():
        """
        Display the help menu.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """

        print("We are here to help you")
        print("*"*50)
        print("""
This is a library management system 
that allows you to borrow books from the library
you can also reserve books that are not available at4 the moment
you can also return books that you have borrowed
you can also pay fines that you have incurred
you can also view your borrowed books
you can also view your reserved books
you can also view your returned books
you can also view your lost books
Etc
        """)
        print("*"*50)
        LibraryManagementSystem.menu()

    @staticmethod
    def exit():
        """
        Exit the Library Management System.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """

        print("Thanks for using Library Management System")
        print("Goodbye")

    def __repr__(self):
        return f"LibraryManagementSystem()"


libraryManagementSystem = LibraryManagementSystem()
# %%
