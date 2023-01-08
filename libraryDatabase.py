###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###


from book import Book
import json
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute(""" CREATE TABLE 
            books (
                    bookID text, 
                    title text, 
                    authors text, 
                    isbn text PRIMARY KEY, 
                    publisher text, 
                    publication_date text,
                    available integer
            ) """)


class LibraryDatabase:
    """ 
    LibraryDatabase class to represent the database for the library
    """

    list_of_books = {}
    def __init__(self):
        pass
        
    @classmethod  
    def loadBooks(cls):
        """
        Loads books from books.json into database
        """
        try:
            data = []
            with conn:
                c.execute('SELECT * FROM books')
            data = c.fetchall()

            if len(data) == 0:
                with open('books2.json') as fileData:
                    books = json.load(fileData)
                    for book in books:
                        newBook = Book(
                            book["bookID"], 
                            book["title"],
                            book["authors"],
                            book["isbn"],
                            book["publisher"],
                            book["publication_date"]
                        )
                        LibraryDatabase.insertBook(newBook)
                    
                    print("All books loaded")

            else:
                print("Data already in database")

        except Exception as e:
            print(e)
            print("Error loading books")

    @classmethod
    def insertBook(cls, book):
        """ 
        Inserts book into database

        Parameters
        ----------
        book : Book
            Book object to be inserted into database

        Returns
        -------
        bool
            True if book is inserted into database

        """
        with conn:
            c.execute("""INSERT INTO books 
                         VALUES(
                            :bookID,
                            :title, 
                            :authors, 
                            :isbn, 
                            :publisher, 
                            :publication_date, 
                            :available
                        )""",
                      {
                        'bookID': book.bookID, 
                        'title': book.title, 
                        'authors': book.authors, 
                        'isbn': book.isbn, 
                        'publisher': book.publisher, 
                        'publication_date': book.publication_date,
                        'available': book.available
                        }
                    )
            return True

    @classmethod
    def getBooks(cls):
        """ 
        Returns all books in database
        """

        with conn:
            c.execute('SELECT * FROM books')
        return c.fetchall()

    @classmethod
    def getBook(cls, isbn):
        """ 
        Returns book with isbn

        Parameters
        ----------
        isbn : str
            isbn of book to be returned

        Returns
        -------
        list
            List of book with isbn

        """ 
        
        with conn:
            c.execute('SELECT * FROM books WHERE isbn = :isbn',{'isbn': isbn})
        data = c.fetchall()

        if len(data) == 0:
            print("Books is not in database")

        return data

    @classmethod
    def deleteBook(cls, isbn):
        """
        Deletes book with isbn

        Parameters
        ----------
        isbn : str
            isbn of book to be deleted

        Returns
        -------
        bool
            True if book is deleted

        """

        check = LibraryDatabase.getBook(isbn)
        if len(check) != 0:
            with conn:
                c.execute('DELETE FROM books WHERE isbn=:isbn', 
                        {'isbn': isbn})
                print("Book deleted")
                return True

    @classmethod
    def searchByField(cls, field, search):
        """ 
        Searches for book by field

        Parameters
        ----------
        field : str
            Field to search for book

        search : str
            Search term

        Returns
        -------
        list
            List of books with search term in field

        """

        search = '%'+search+'%'
        cmd = f'SELECT * FROM books WHERE {field} LIKE :search'
        if field in ['title', 'authors', 'publisher', 'publication_date', 'isbn']:
            c.execute(cmd, {'search': search})
        else:
            c.execute('SELECT * FROM books WHERE authors LIKE :search',
             {'search': search})

        data = c.fetchall()

        if len(data) == 0:
            print(f"No book found for {field} : {search}")

        return data

    @classmethod
    def search(cls, search):
        """
        Searches for book by all fields

        Parameters
        ----------
        search : str
            Search term

        Returns
        -------
        list
            List of books with search term in all fields

        """

        search = '%'+search+'%'
        cmd = f'SELECT * FROM books WHERE title LIKE :search OR authors LIKE :search OR publisher LIKE :search OR publication_date LIKE :search OR isbn LIKE :search'
        c.execute(cmd, {'search': search})

        data = c.fetchall()

        if len(data) == 0:
            print(f"No book found for search : {search}")

        return data

    @classmethod
    def updateBook(cls, book):
        """
        Updates book in database

        Parameters
        ----------
        book : Book
            Book object to be updated

        Returns
        -------
        bool
            True if book is updated

        """

        with conn:
            c.execute("""UPDATE books SET 
                        bookID = :bookID,
                        title = :title, 
                        authors = :authors, 
                        isbn = :isbn, 
                        publisher = :publisher, 
                        publication_date = :publication_date, 
                        available = :available
                        WHERE isbn=:isbn""",
                      {
                        'bookID': book.bookID, 
                        'title': book.title, 
                        'authors': book.authors, 
                        'isbn': book.isbn, 
                        'publisher': book.publisher, 
                        'publication_date': book.publication_date,
                        'available': book.available
                        }
                    )
            return True

    def __repr__(self):
        """ 
        Returns string representation of LibraryDatabase object
        """
        return f"LibraryDatabase({self.list_of_books})"