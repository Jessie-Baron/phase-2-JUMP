from flask import Blueprint, Flask, request, jsonify
import connection as conn
import query_data as db


category_routes = Blueprint('author', __name__)

@category_routes.route("")
def books():
    books = db.all_books(conn.create_connection("bims.db"))

    return jsonify(books)

@category_routes.route('/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
        connection = conn.create_connection('bims.db')

        book = db.select_category(connection, category_id, column='id')
        return jsonify(book)
