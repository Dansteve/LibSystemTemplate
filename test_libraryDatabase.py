###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###

#%%
import pytest
from libraryDatabase import LibraryDatabase
from book import Book

#%%
# load books

class TestLibraryDatabase:

    library_db = LibraryDatabase()

    def test_loadBooks(self):
        self.library_db.loadBooks()
        assert len(self.library_db.getBooks()) > 0

    @pytest.mark.parametrize("bookID, title, authors, isbn, publisher, publishedDate, available", 
    [("123456", "The Book of Life", "Dansteve Adekanbi", "978-3-16-148410-0", "Dansteve", "2020-01-01", 10),
    ("123457", "The Book of Life 2", "Dansteve Adekanbi", "978-3-16-148410-1", "Dansteve", "2020-01-01", 10),
    ("123458", "The Book of Life 3", "Dansteve Adekanbi", "978-3-16-148410-2", "Dansteve", "2020-01-01", 10),])
    def test_insertBook(self, bookID, title, authors, isbn, publisher, publishedDate, available):
        newBook = Book(bookID, title, authors, isbn, publisher, publishedDate, available)
        assert  self.library_db.insertBook(newBook) == True
        
    @pytest.mark.parametrize("isbn", ["978-3-16-148410-0", "978-3-16-148410-1", "978-3-16-148410-2"])
    def test_getBook(self, isbn):
        assert len(self.library_db.getBook(isbn)) > 0 

    @pytest.mark.parametrize("bookID, title, authors, isbn, publisher, publishedDate, available",
    [("123456", "The Book of Life", "Steve Adekanbi", "978-3-16-148410-0", "Adekanbi", "2020-01-01", 10),
    ("123457", "The Book of Life 2", "Steve Adekanbi", "978-3-16-148410-1", "Adekanbi", "2020-01-01", 10),
    ("123458", "The Book of Life 3", "Steve Adekanbi", "978-3-16-148410-2", "Adekanbi", "2020-01-01", 10), ])
    def test_updateBook(self, bookID, title, authors, isbn, publisher, publishedDate, available):
        updateBook = Book(bookID, title, authors, isbn, publisher, publishedDate, available)
        assert self.library_db.updateBook(updateBook) == True

    @pytest.mark.parametrize("isbn", ["978-3-16-148410-0", "978-3-16-148410-1", "978-3-16-148410-2"])
    def test_searchByField(self, isbn):
        assert len(self.library_db.searchByField('isbn', isbn)) > 0

    @pytest.mark.parametrize("isbn", ["978-3-16-148410-0"])
    def test_deleteBook(self, isbn):
        currentBookCount = len(self.library_db.getBooks())
        self.library_db.deleteBook(isbn)
        assert len(self.library_db.getBooks()) == currentBookCount - 1

    @pytest.mark.parametrize("isbn", ["978-3-16-148410-0"])
    def test_getBook(self, isbn):
        assert len(self.library_db.getBook(isbn)) > 0 

    @pytest.mark.parametrize("search", ["978-3-16-148410-1", "978-3-16-148410-2"])
    def test_search(self, search):
        assert len(self.library_db.search(search)) > 0

