# Written by Mateusz Rzeczyca

from flask import Flask
from flask_restful import Resource, reqparse ,Api
import json

TGS = Flask(__name__)
api = Api(TGS)

class BooksApi(Resource):
    def __init__(self):
        with open('books.json') as f:
            json_data = json.load(f)

        self.books = json_data["books"]


    def get(self, id):
        for book in self.books:
            if(id == book["id"]):
                return book, 200
        return "Book not found", 404


    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("language")
        parser.add_argument("edition")
        parser.add_argument("author")
        args = parser.parse_args()

        for book in self.books:
            if(id == book["id"]):
                return "Id {} already exists".format(id), 400

        book = {
            "id": id,
            "language": args["language"],
            "edition": args["edition"],
            "author": args["author"]
        }

        self.books.append(book)
        return book, 201


    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("language")
        parser.add_argument("edition")
        parser.add_argument("author")
        args = parser.parse_args()

        for book in self.books:
            if(id == book["id"]):
                book["language"] = args["language"]
                book["edition"] = args["edition"]
                book["author"] = args["author"]
                return book, 200

        book = {
            "id": id,
            "language": args["language"],
            "edition": args["edition"],
            "author": args["author"]
        }

        self.books.append(book)
        return book, 201

    
    def delete(self, id):
        self.books = [book for book in self.books if book["id"] != id]
        return "{} is deleted.".format(id), 200

api.add_resource(BooksApi, "/id/<string:id>")

TGS.run(debug=True, port=8080)