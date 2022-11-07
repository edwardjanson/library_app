import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book_1 = Book("Ready Player One", "Ernest Cline", "Science Fiction")
    
    def test_book_has_title(self):
        self.assertEqual("Ready Player One", self.book_1.title)
    
    def test_book_has_author(self):
        self.assertEqual("Ernest Cline", self.book_1.author)
    
    def test_book_has_genre(self):
        self.assertEqual("Science Fiction", self.book_1.genre)
    
    def test_update_check_out_status_to_checked_out(self):
        self.book_1.update_check_out(["checked-out"])
        self.assertEqual(True, self.book_1.is_checked_out)
    
    def test_update_check_out_status_to_checked_in(self):
        self.book_1.update_check_out(["checked-in"])
        self.assertEqual(False, self.book_1.is_checked_out)

    def test_hyphenate_title(self):
        hyphenated_title = self.book_1.hyphenate_title()
        self.assertEqual("ready-player-one", hyphenated_title)
    
    def test_new_check_out_is_logged(self):
        self.book_1.update_check_out(["checked-out"])
        self.assertEqual(len(self.book_1.check_out_logs), 1)
    