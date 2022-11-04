book_list = []

def get_book(hyphenated_title):
    for book in book_list:
        if book.hyphenate_title() == hyphenated_title:
            return book

def add_book(book):
    book_list.append(book)

def remove_book(book):
    book_list.remove(book)

def update_check_out_status(book_to_update, status):
    for book in book_list:
        if book_to_update == book:
            book.update_check_out(status)