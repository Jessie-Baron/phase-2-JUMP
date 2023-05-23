from flask import Blueprint, Flask, request, jsonify
import api.book_routes as br
import api.author_routes as ar
import api.category_routes as cr
from datetime import datetime
import connection as conn
import query_data as db

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to my App!"

@app.route("/hello/<name>", methods=["GET"])
def say_hello(name):
    return f"Hello {name}"

@app.route("/about")
def about():
    print(request.args)
    return "about me"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return f"Please Log in"
    elif request.method == "POST":
        print(request)
        print(request.json)
        if request.json["username"] == "Hello" and request.json["password"] == "World":
            return "Thank you for logging in"
        else:
            return "Incorrect Username or Password"

@app.route("/date/today")
def send_date():
    today = datetime.now()
    data = {
        "day": today.day,
        "month": today.month,
        "year": today.year
    }
    # return f"<h1>{today}</h1>"
    return jsonify(data)


app.register_blueprint(ar.publisher_routes, url_prefix='/api/publisher')
app.register_blueprint(cr.category_routes, url_prefix='/api/category')
app.register_blueprint(br.book_routes, url_prefix='/api/book')
# @app.route("/book")
# def books():
#     books = db.all_books(conn.create_connection("bims.db"))

#     return jsonify(books)

# @app.route('/book/<int:id>', methods=['GET'])
# def get_book_by_id(book_id):
#         connection = conn.create_connection('bims.db')

#         book = db.select_book(connection, book_id)
#         return jsonify(book)

# @app.route("/author")
# def authors():
#     books = db.all_books(conn.create_connection("bims.db"))

#     return jsonify(authors)

# @app.route('/author/<int:id>', methods=['GET'])
# def get_author_by_id(author_id):
#         connection = conn.create_connection('bims.db')

#         author = db.select_author(connection, author_id)
#         return jsonify(author)

# @app.route("/category")
# def categories():
#     categories = db.all_books(conn.create_connection("bims.db"))

#     return jsonify(categories)

# @app.route('/category/<int:id>', methods=['GET'])
# def get_category_by_id(category_id):
#         connection = conn.create_connection('bims.db')

#         category = db.select_book(connection, category_id)
#         return jsonify(category)

if __name__ == "__main__":
    app.run(debug=True)
