from flask import render_template, redirect, request
from models.book import Book
from models.books import book_list, get_book, add_book, remove_book, update_check_out_status
from app import app


@app.route("/books")
def books():
    return render_template("books.html", books=book_list, error=False)

@app.route("/books/<hyphenated_title>")
def detail(hyphenated_title):
    book = get_book(hyphenated_title)
    return render_template("book.html", book=book)

@app.route("/books/create", methods=["POST"])
def create_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]

    # Show error message if a form field is missing
    if book_title == "" or book_author == "" or book_genre == "":
        return render_template("books.html", books=book_list, error=True) 

    new_book = Book(book_title, book_author, book_genre)
    add_book(new_book)
    return redirect("/books")

@app.route("/books/search", methods=["GET"])
def search_book():
    title = request.args.get("title")
    author = request.args.get("author")
    genre = request.args.get("genre")

    # Return a list of books that matches the search
    updated_books_list = book_list.copy()
    for book in book_list:
        if title and title not in book.title:
            updated_books_list.remove(book)
            continue
        if author and author not in book.author:
            updated_books_list.remove(book)
            continue
        if genre and genre not in book.genre:
            updated_books_list.remove(book)
            continue
    
    return render_template("books.html", books=updated_books_list, error=False)

@app.route('/books/<hyphenated_title>/delete', methods=['POST'])
def delete_book(hyphenated_title):
    book = get_book(hyphenated_title)
    remove_book(book)
    return redirect("/books")

@app.route('/books/<hyphenated_title>/update', methods=['POST'])
def update_book_check_out_status(hyphenated_title):
    # Update the check-out status based on user selection
    book = get_book(hyphenated_title)
    status = request.form.getlist("check-out-status")
    update_check_out_status(book, status)

    # Load page where the form submission occurred
    location = request.args.get("loc")
    if location == "book":
        return render_template("book.html", book=book)
    else:
        return redirect("/books")