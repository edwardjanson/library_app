class Books:

    def __init__(self):
        self.book_list = []

    def get_book(self, hyphenated_title):
        for book in self.book_list:
            if book.hyphenate_title() == hyphenated_title:
                return book

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)

    def update_check_out_status(self, book_to_update, status):
        for book in self.book_list:
            if book_to_update == book:
                book.update_check_out(status)