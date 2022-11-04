from flask import render_template, redirect, request
from models.book import Book
from models.books import book_list, get_book, add_book, remove_book
from app import app


@app.route("/books", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        try:
            book_title = request.form["title"]
            book_author = request.form["author"]
            book_genre = request.form["genre"]
            new_book = Book(book_title, book_author, book_genre)
            add_book(new_book)
            return render_template("books.html", books=book_list)
        except KeyError:
            print(request.form)
            print(request.form.getlist("check-out-status"))
            return render_template("books.html", books=book_list)
    else:
        return render_template("books.html", books=book_list)

@app.route("/books/<hyphenated_title>")
def detail(hyphenated_title):
    return render_template("book.html", book=get_book(hyphenated_title))

@app.route('/books/<hyphenated_title>/delete', methods=['POST'])
def delete_book(hyphenated_title):
    book = get_book(hyphenated_title)
    remove_book(book)
    return redirect('/books')