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

if __name__ == "__main__":
    app.run(debug=True)
