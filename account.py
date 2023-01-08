###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###

import datetime
import json


class Account:
    """
    Account class for the Library Management System.\n
    This class is used to create account objects for the Library Management System.\n
    The account objects are used to store the information of the users of the Library Management System.\n
    The account objects are also used to authenticate the users of the Library Management System.\n
    The account objects are also used to store the information of the books borrowed, reserved, returned and lost by the users of the Library Management System.\n
    The account objects are also used to store the fines incurred by the users of the Library Management System.\n
    The account objects are also used to store the information of the users of the Library Management System.\n
    """

    __MAX_LOAN_PERIOD = 7
    # fine per day is 10 pennies which is 0.1 pound
    __FINE_PER_DAY = 0.1
    # fine per lost book is 100 pound
    __FINE_PER_BOOK = 100

    def __init__(self, a_id, password, f_name, l_name, l_books_borrowed=[], l_books_reserved=[],
                 l_return_books=None, l_lost_books=None, acc_fine=None, userType=None):
        self.a_id = a_id
        self.password = password
        self.f_name = f_name
        self.l_name = l_name
        self.l_books_borrowed = l_books_borrowed
        self.l_books_reserved = l_books_reserved
        self.l_return_books = l_return_books
        self.l_lost_books = l_lost_books
        self.acc_fine = acc_fine
        self.userType = userType

    @classmethod
    def load_account(cls, a_id):
        """
        Load an account from the accounts.json file.

        Parameters:
        ----------
            a_id (int): The account id.

        Returns:
        --------
            A tuple containing the account object and the account type.
            (Account, userType) or (None, None)


        Raises:
            None
        """
        try:
            with open("accounts.json") as fd:
                acc = json.load(fd)
                userType = Account.get_account_type(a_id)
                if (userType != "undefined"):
                    if (acc[userType][a_id]):
                        return Account(acc[userType][a_id]["id"],
                                    acc[userType][a_id]["password"],
                                    acc[userType][a_id]["f_name"],
                                    acc[userType][a_id]["l_name"],
                                    acc[userType][a_id]["l_books_borrowed"],
                                    acc[userType][a_id]["l_books_reserved"],
                                    acc[userType][a_id]["l_return_books"],
                                    acc[userType][a_id]['l_lost_books'],
                                    acc[userType][a_id]["acc_fine"],
                                    userType
                                    ), userType
                    else:
                        return None, None
                else:
                    return None, None

        except FileNotFoundError:
            print("accounts.json not found")
            return None, None

    @classmethod
    def load_init_all_accounts(cls):
        """
        Load all accounts from the accounts.json file.

        Parameters:
            None

        Returns:
            A dictionary containing all accounts. 
            See the example below for the format of the dictionary.\n
            {
                [userType]: {
                    "[userType]0001": {
                        "id": "0001",
                        "password": "password",
                        "f_name": "John",
                        "l_name": "Doe",
                        "l_books_borrowed": [],
                        "l_books_reserved": [],
                        "l_return_books": [],
                        "l_lost_books": [],
                        "acc_fine": 0
                    },
                    ...
                },
                ...
            }


        """
        # load all accounts form accounts-init and replace the current accounts.json
        try:
            with open("accounts-init.json") as fd:
                acc = json.load(fd)
                with open("accounts.json", "w") as fd:
                    json.dump(acc, fd, indent=4)
                    print("All accounts loaded")

        except FileNotFoundError:
            print("accounts-init.json not found")

        except Exception as e:
            print(e)
            print("Error loading accounts")

    @staticmethod
    def get_account_type(a_id):
        """
        Get the account type from the account id.

        Parameters:
            a_id (int): The account id.

        Returns:
            The account type or undefined if the account type is not found.

        Raises:
            None
        """
        
        return {
            "stude": "student",
            "staff": "staff",
            "libra": "librarian"
        }.get(a_id[0:5], 'undefined')

    @staticmethod
    def create_account(a_id, password, f_name, l_name, userType, class_or_department=None):
        """
        Create a new account.

        Parameters:
            a_id (int): The account id.
            password (str): The account password.
            f_name (str): The account first name.
            l_name (str): The account last name.
            userType (str): The account type.
            class_or_department (str): The account class or department.

        Returns:
            Boolean value.
            True if the account is created successfully, False otherwise.

        Raises:
            None

        """
        with open("accounts.json") as fd:
            acc = json.load(fd)
            # check if account already exist
            if (f"{userType}{a_id}" in acc[userType]):
                return False
            else:
                userData = {
                    "id": a_id,
                    "password": password,
                    "f_name": f_name,
                    "l_name": l_name,
                    "l_books_borrowed": [],
                    "l_books_reserved": [],
                    "l_return_books": [],
                    "l_lost_books": [],
                    "acc_fine": 0,
                }
                # user type is student add class if not add department
                if (userType == "student"):
                    userData["class"] = class_or_department
                else:
                    userData["department"] = class_or_department

                acc[userType][f"{userType}{a_id}"] = userData

                with open("accounts.json", "w") as fd:
                    fd.write(json.dumps(acc, indent=4))
                    # json.dump(acc, fd, indent=4)
                return True

    @staticmethod
    def remove_account(a_id):
        """
        Remove an account.

        Parameters:
            a_id (int): The account id.

        Returns:
            Boolean value.
            True if the account is removed successfully, False otherwise.

        Raises:
            None
        """
        with open("accounts.json") as fd:
            acc = json.load(fd)
            userType = Account.get_account_type(a_id)
            if (userType != "undefined"):
                if (acc[userType][a_id]):
                    del acc[userType][a_id]
                    with open("accounts.json", "w") as fd:
                        json.dump(acc, fd, indent=4)
                    return True
                else:
                    return False
            else:
                return False
                
    # update account json with l_books_borrowed | l_books_reserved | l_return_books | l_lost_books acc_fine
    def update_account_json(self):
        """
        Update the current account object to the account json file.

        Parameters:
            None

        Returns:
            None

        """

        # Open the JSON file in read mode
        with open('accounts.json', 'r') as json_file:
            # Load the JSON data into a Python dictionary
            data = json.load(json_file)

            # Update the data in the dictionary
            data[self.userType][f"{self.userType}{self.a_id}"]['l_books_borrowed'] = self.l_books_borrowed
            data[self.userType][f"{self.userType}{self.a_id}"]['l_books_reserved'] = self.l_books_reserved
            data[self.userType][f"{self.userType}{self.a_id}"]['l_return_books'] = self.l_return_books
            data[self.userType][f"{self.userType}{self.a_id}"]['l_lost_books'] = self.l_lost_books
            data[self.userType][f"{self.userType}{self.a_id}"]['acc_fine'] = self.set_account_fine()

            # Convert the updated dictionary back into a JSON string
            json_data = json.dumps(data, indent=4)

        # Open the JSON file in write mode and write the updated JSON string to the file
        with open('accounts.json', 'w') as json_file:
            json_file.write(json_data)

        # Close the file to save the changes
        json_file.close()

    def late_return_fees(self):
        """
        Calculate the late return fees for the current account.
        and print the late fees for each book.

        Parameters:
            None

        Returns:
            None

        """
        
        for b in self.l_books_borrowed:
            if (self.get_days_overlap(b['date_borrowed']) > 0):
                print(
                    f"""Book: {b['isbn']} is late by {self.get_days_overlap(b['date_borrowed'])} days""")

    def set_account_fine(self):
        """
        Set the total fine for the current account.

        Parameters:
            None

        Returns:
            The total fine for the current account.

        """

        self.acc_fine = self.get_total_late_fees() + self.get_total_lost_fees()
        return self.acc_fine

    def get_total_late_fees(self):
        """
        Calculate the total late fees for the current account.

        Parameters:
            None

        Returns:
            The total late fees for the current account.
        """

        total_fine = 0

        for b in self.l_books_borrowed:
            # check if book has fine and if it is paid
            
            total_fine += self.get_late_fine(b['date_borrowed'])
        return total_fine

    def get_total_lost_fees(self):
        """
        Calculate the total lost fees for the current account.

        Parameters:
            None

        Returns:
            The total lost fees for the current account.

        """

        total_fine = 0
        for _ in self.l_lost_books:
            # check if hasPaidFine is true or false
            if (self.l_lost_books[_]['has_paid'] == False):
                total_fine += self.__FINE_PER_BOOK
        return total_fine

    def get_late_fine(self, date):
        """
        Calculate the late fees for the current account.

        Parameters:
            date (str): The date the book was borrowed.

        Returns:
            The late fees for the current account.

        """
        return self.get_days_overlap(date) * self.__FINE_PER_DAY

    def get_days_overlap(self, date):
        """
        Calculate how many days the books borrowed were late.

        Parameters:
            date (str): The date the book was borrowed.

        Returns:
            The number of days the books borrowed were late.

        """

        date = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S")
        date_laps = (datetime.datetime.now() - date).days
        if date_laps > self.__MAX_LOAN_PERIOD:
            return date_laps - self.__MAX_LOAN_PERIOD
        else:
            return 0

    def __repr__(self):
        """
        Return a string representation of the current account object.
        """

        return f"""{'*'*20}
Id: {self.a_id}
First name: {self.f_name}
Last name: {self.l_name}
Books borrowed: {self.l_books_borrowed}
Books reserved: {self.l_books_reserved}
History return: {self.l_return_books}
Lost books: {self.l_lost_books}
Fine: Pounds(£) {self.set_account_fine():,} 
    """
