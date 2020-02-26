# Written by Mateusz Rzeczyca

from flask import Flask
from flask_restful import Resource, reqparse ,Api
import json


TGS = Flask(__name__)
api = Api(TGS)


class BooksApi(Resource):
    """
    Class, which we need for creating API endpoints and the required REST methods

    Attributes:
        books(list): containts the whole data of JSON file
    """
    def __init__(self):
        """
        Reads content of JSON file and save it to books variable
        """
        with open('books.json', 'r') as f:
            json_data = json.load(f)

        self.books = json_data["books"]


    def get(self, id):
        """
        Searches requested id in list of books, and will return the data if found along with 
        response code 200 OK. Otherwise 404 not found
        """
        for book in self.books:
            if(id == book["id"]):
                return book, 200

        return "Book not found", 404


    def post(self, id):
        """
        Inserts new book data in list of books and returns inserted data with response code 201 created. 
        If record already exists it returns error code 400 bad request.
        """
        parser = reqparse.RequestParser()
        parser.add_argument("title")
        parser.add_argument("edition")
        parser.add_argument("author")
        args = parser.parse_args()

        for book in self.books:
            if(id == book["id"]):
                return "Id {} already exists".format(id), 400

        book = {
            "id": id,
            "title": args["title"],
            "edition": args["edition"],
            "author": args["author"]
        }

        self.books.append(book)
        #self.rewrite()
        return book, 201


    def put(self, id):
        """
        Overwrites record and returns data along with response code 200 OK. If record does not exist, 
        it creates the data and returns it with response code 201 created.
        """
        parser = reqparse.RequestParser()
        parser.add_argument("title")
        parser.add_argument("edition")
        parser.add_argument("author")
        args = parser.parse_args()

        for book in self.books:
            if(id == book["id"]):
                book["title"] = args["title"]
                book["edition"] = args["edition"]
                book["author"] = args["author"]
                return book, 200

        book = {
            "id": id,
            "title": args["title"],
            "edition": args["edition"],
            "author": args["author"]
        }

        self.books.append(book)
        #self.rewrite()
        return book, 201

    
    def delete(self, id):
        """
        Deletes the record if exist and returns the data with response code 200 OK. 
        Otherwise 404 not found.
        """
        self.books = [book for book in self.books if book["id"] != id]
        #self.rewrite()
        return "{} is deleted.".format(id), 200


    def rewrite(self):
        """
        Writing changes to JSON file in order to save what we have accomplished during session.
        """
        with open("books.json", "w") as f:
            f.seek(0)
            data = '{ "books": ' + self.books + '}'
            json.dump(data, f)
            f.truncate()


api.add_resource(BooksApi, "/books/<string:id>")

TGS.run(debug=True, port=8080)