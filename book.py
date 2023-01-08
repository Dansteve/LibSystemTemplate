###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###

class Book:
    """
    Book class to represent a book in the library
    """

    def __init__(self, bookID, title, authors, isbn, publisher, publication_date, available=5):
        self.__bookID = bookID
        self.__title = title
        self.__authors = authors
        self.__isbn = isbn
        self.__publisher = publisher
        self.__publication_date = publication_date
        self.__available = available

    @property
    def bookID(self):
        return self.__bookID

    @bookID.setter
    def bookID(self, bookID):
        self.__bookID = bookID

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        self.__authors = authors

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    @property
    def publication_date(self):
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        self.__publication_date = publication_date
    
    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, available):
        self.__available = available

    def reservation_status(self):
        """
        Returns the status of the book for reservation

        Returns:
            str: "Available for Reservation" if available for reservation
            str: "Not Available for Reservation, please check back later for availability or borrow book" if not available for reservations
        """
        if self.__available == 0:
            return "Available for Reservation"
        else:
            return "Not Available for Reservation, please check back later for availability or borrow book"

    def __repr__(self):
        """
        Returns the string representation of the book object
        """
        return f"""Book(
            Book ID: {self.__bookID}, 
            Title: {self.__title}, 
            Authors: {self.__authors}, 
            ISBN: {self.__isbn}, 
            Publisher: {self.__publisher}, 
            Publication Date: {self.__publication_date}, 
            Available: {self.__available})
            """


