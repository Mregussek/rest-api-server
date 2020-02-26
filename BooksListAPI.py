# Written by Mateusz Rzeczyca

from flask_restful import Resource, reqparse
import json


class BooksListAPI(Resource):
    """
    Class, which we need for creating API endpoint and the required REST methods
    Used for /books URL.

    Attributes:
        books(list): contains the whole data of JSON file
        parser(flask_restful.reqparse.RequestParser): handles requests
    """

    def __init__(self):
        """
        Reads content of JSON file and save it to books variable, prepares
        object for handling requests
        """
        with open('books.json', 'r') as f:
            json_data = json.load(f)

        self.books = json_data["books"]

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("id", type=str, required=True,
                                 help='No book id provided', location='json')
        self.parser.add_argument("title", type=str, required=True,
                                 help='No book title provided', location='json')
        self.parser.add_argument("edition", type=str, default='Not given',
                                 location='json')
        self.parser.add_argument("author", type=str, required=True,
                                 help='No book author provided', location='json')

    def get(self):
        """
        Searches requested id in list of books, and will return the data if found along with
        response code 200 OK. Otherwise 404 not found
        """
        if self.books is not None:
            return self.books, 200
        else:
            return "Books not found", 404

    def post(self):
        """
        Inserts new book data in list of books and returns inserted data with response code 201 created.
        If record already exists it returns error code 400 bad request.
        """
        args = self.parser.parse_args()

        for book in self.books:
            if args["id"] == book["id"]:
                return "Id {} already exists".format(id), 400

        book = {
            "id": args["id"],
            "title": args["title"],
            "edition": args["edition"],
            "author": args["author"]
        }

        self.books.append(book)
        return book, 201

    def put(self):
        """
        Overwrites record and returns data along with response code 200 OK. If record does not exist,
        it creates the data and returns it with response code 201 created.
        """
        args = self.parser.parse_args()

        for book in self.books:
            if args["id"] == book["id"]:
                book["title"] = args["title"]
                book["edition"] = args["edition"]
                book["author"] = args["author"]
                return book, 200

        book = {
            "id": args["id"],
            "title": args["title"],
            "edition": args["edition"],
            "author": args["author"]
        }

        self.books.append(book)
        return book, 201

    def delete(self):
        """
        Deletes the record if exist and returns the data with response code 200 OK.
        Otherwise 404 not found.
        """
        args = self.parser.parse_args()
        self.books = [book for book in self.books if book["id"] != args["id"]]
        return "{} is deleted.".format(id), 200
