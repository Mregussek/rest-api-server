# Written by Mateusz Rzeczyca
# info@mateuszrzeczyca.pl
# 13.03.2020

from flask import Flask
from flask_restful import Api

from BooksAPI import BooksAPI
from BooksListAPI import BooksListAPI


if __name__ == "__main__":
    rest_app = Flask(__name__)
    api = Api(rest_app)

    api.add_resource(BooksListAPI, "/books", endpoint="books")
    api.add_resource(BooksAPI, "/books/<string:id>", endpoint="book")

    rest_app.run(host='0.0.0.0', debug=True, port=8080)
