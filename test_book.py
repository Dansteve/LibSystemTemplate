###
# Name: Dansteve Adekanbi
# Student ID: 22178806
# Course Title: CMP7244 Software Development
# Course Code: CMP7244
###

#%%
import pytest
from book import Book

#%%
# load books

class TestBook:

    @pytest.mark.parametrize("bookID, title, authors, isbn, publisher, publication_date, available",
                             [("123456", "The Book of Life", "Dansteve Adekanbi", "978-3-16-148410-0", "Dansteve", "2020-01-01", 10),
                              ("123457", "The Book of Life 2", "Dansteve Adekanbi",
                                 "978-3-16-148410-1", "Dansteve", "2020-01-01", 10),
                              ("123458", "The Book of Life 3", "Dansteve Adekanbi", "978-3-16-148410-2", "Dansteve", "2020-01-01", 10) ])
    def test_book(self, bookID, title, authors, isbn, publisher, publication_date, available):
        newBook = Book(bookID, title, authors, isbn, publisher, publication_date, available)
        assert newBook.bookID == bookID
        assert newBook.title == title
        assert newBook.authors == authors
        assert newBook.isbn == isbn
        assert newBook.publisher == publisher
        assert newBook.publication_date == publication_date
        assert newBook.available == available
   


    @pytest.mark.parametrize("bookID, title, authors, isbn, publisher, publication_date, available",
                             [("123456", "The Book of Life", "Dansteve Adekanbi", "978-3-16-148410-0", "Dansteve", "2020-01-01", 0),
                              ("123457", "The Book of Life 2", "Dansteve Adekanbi", "978-3-16-148410-1", "Dansteve", "2020-01-01", 10),
                              ("123458", "The Book of Life 3", "Dansteve Adekanbi", "978-3-16-148410-2", "Dansteve", "2020-01-01", 0)])
    def test_reservation_status(self, bookID, title, authors, isbn, publisher, publication_date, available):
        newBook = Book(bookID, title, authors, isbn, publisher, publication_date, available)
        if available == 0:
            assert newBook.reservation_status() == "Available for Reservation"
        else:
            assert newBook.reservation_status(
            ) == "Not Available for Reservation, please check back later for availability or borrow book"
