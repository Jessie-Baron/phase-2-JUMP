from flask import Blueprint, Flask, request, jsonify
import connection as conn
import query_data as db


book_routes = Blueprint('book', __name__)

@book_routes.route("")
def books():
    books = db.all_books(conn.create_connection("bims.db"))

    return jsonify(books)

@book_routes.route('/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
        print(book_id)
        connection = conn.create_connection('bims.db')

        book = db.select_book(connection, book_id)
        return jsonify(book)
