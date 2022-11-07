import unittest
from models.books import Books
from models.book import Book

class TestBooks(unittest.TestCase):
    
    def setUp(self):
        self.books = Books()
        self.book_1 = Book("Ready Player One", "Ernest Cline", "Science Fiction")

    def test_adding_book(self):
        self.books.add_book(self.book_1)
        self.assertEqual(len( self.books.book_list), 1)
    
    def test_get_book_by_hyphenated_title(self):
        self.books.add_book(self.book_1)
        book = self.books.get_book("ready-player-one")
        self.assertEqual(book, self.book_1)
    
    def test_removing_book(self):
        self.books.add_book(self.book_1)
        self.assertEqual(len(self.books.book_list), 1)
        self.books.remove_book(self.book_1)
        self.assertEqual(len(self.books.book_list), 0)

    def test_updating_check_out_status_to_checked_in(self):
        self.books.add_book(self.book_1)
        self.books.update_check_out_status(self.book_1, ["checked-in"])
        check_out_status = self.book_1.is_checked_out
        self.assertEqual(False, check_out_status)
    
    def test_updating_check_out_status_to_checked_out(self):
        self.books.add_book(self.book_1)
        self.books.update_check_out_status(self.book_1, ["checked-out"])
        check_out_status = self.book_1.is_checked_out
        self.assertEqual(True, check_out_status)