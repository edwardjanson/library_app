book_list = []

def get_book(hyphenated_title):
    for book in book_list:
        if book.hyphenate_title() == hyphenated_title:
            return book

def add_book(book):
    book_list.append(book)

def remove_book(book):
    book_list.remove(book)