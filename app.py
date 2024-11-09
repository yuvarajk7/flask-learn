from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

books = []


@app.route("/books", methods=["POST"])
@swag_from("swagger/create_book.yml")
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201


@app.route("/books", methods=["GET"])
@swag_from("swagger/get_books.yml")
def get_books():
    return jsonify(books)


@app.route("/books/<int:book_id>", methods=["GET"])
@swag_from("swagger/get_book.yml")
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"message": "Book not found"}), 404
    return jsonify(book)


@app.route("/books/<int:book_id>", methods=["PUT"])
@swag_from("swagger/update_book.yml")
def update_book(book_id):
    updated_book = request.get_json()
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"message": "Book not found"}), 404
    book.update(updated_book)
    return jsonify(book)


@app.route("/books/<int:book_id>", methods=["DELETE"])
@swag_from("swagger/delete_book.yml")
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 204


if __name__ == "__main__":
    app.run(debug=True)
