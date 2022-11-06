from flask import render_template, redirect, request
from models.book import Book
from models.books import book_list, get_book, add_book, remove_book, update_check_out_status
from app import app


@app.route("/books", methods=["GET"])
def books():
    if request.method == "GET":
        title = request.args.get("search")
        author = request.args.get("author")
        genre = request.args.get("author")

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
    print(f"book_title = {book_title}")

    if book_title == "" or book_author == "" or book_genre == "":
        return render_template("books.html", books=book_list, error=True) 

    new_book = Book(book_title, book_author, book_genre)
    add_book(new_book)
    return redirect("/books")

@app.route('/books/<hyphenated_title>/delete', methods=['POST'])
def delete_book(hyphenated_title):
    book = get_book(hyphenated_title)
    remove_book(book)
    return redirect("/books")

@app.route('/books/<hyphenated_title>/update', methods=['POST'])
def update_book_check_out_status(hyphenated_title):
    book = get_book(hyphenated_title)
    status = request.form.getlist("check-out-status")
    update_check_out_status(book, status)
    location = request.args.get("loc")
    if location == "book":
        return render_template("book.html", book=book)
    else:
        return redirect("/books")