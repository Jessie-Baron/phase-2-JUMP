from flask import Blueprint, Flask, request, jsonify
import connection as conn
import query_data as db


publisher_routes = Blueprint('publisher', __name__)

@publisher_routes.route("")
def books():
    books = db.all_books(conn.create_connection("bims.db"))

    return jsonify(books)

@publisher_routes.route('/<int:author_id>', methods=['GET'])
def get_author_by_id(author_id):
        connection = conn.create_connection('bims.db')

        book = db.select_author(connection, author_id, column='id')
        return jsonify(book)
