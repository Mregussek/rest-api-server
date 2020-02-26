# Written by Mateusz Rzeczyca

from flask import Flask
from flask_restful import Api

from BooksAPI import BooksAPI
from BooksListAPI import BooksListAPI


if __name__ == "__main__":
    rest_app = Flask(__name__)
    api = Api(rest_app)

    api.add_resource(BooksListAPI, "/books", endpoint="books")
    api.add_resource(BooksAPI, "/books/<string:id>", endpoint="book")

    rest_app.run(debug=True, port=8080)
