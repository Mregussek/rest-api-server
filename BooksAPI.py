# Written by Mateusz Rzeczyca

from flask_restful import Resource, reqparse
from JSONHandler import JSONHandler


class BooksAPI(Resource):
    """
    Class, which we need for creating API endpoint and the required REST methods
    Used for /books/<given id> URL.

    Attributes:
        books(list): contains the whole data of JSON file
        parser(flask_restful.reqparse.RequestParser): handles requests
    """

    def __init__(self):
        """
        Reads content of JSON file and save it to books variable, prepares
        object for handling requests
        """

        self.file_name = 'books.json'
        self.json_handler = JSONHandler()

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str, location='json')
        self.parser.add_argument("edition", type=str, default='Not given', location='json')
        self.parser.add_argument("author", type=str, location='json')

    def get(self, id):
        """
        Searches requested id in list of books, and will return the data if found along with 
        response code 200 OK. Otherwise 404 not found
        """
        self.json_handler.read_json(self.file_name)

        for book in self.json_handler.get_books_list():
            if id == book["id"]:
                return book, 200

        return "Book not found", 404

    def post(self, id):
        """
        Inserts new book data in list of books and returns inserted data with response code 201 created. 
        If record already exists it returns error code 400 bad request.
        """
        self.json_handler.read_json(self.file_name)
        args = self.parser.parse_args()

        for book in self.json_handler.get_books_list():
            if id == book["id"]:
                return "Id {} already exists".format(id), 400

        book = {
            "id": id,
            "title": args["title"],
            "edition": args["edition"],
            "author": args["author"]
        }

        self.json_handler.append_new_element(book)
        self.json_handler.write_json(self.file_name)
        return book, 201

    def put(self, id):
        """
        Overwrites record and returns data along with response code 200 OK. If record does not exist, 
        it creates the data and returns it with response code 201 created.
        """
        self.json_handler.read_json(self.file_name)
        args = self.parser.parse_args()

        for book in self.json_handler.get_books_list():
            if id == book["id"]:
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

        self.json_handler.append_new_element(book)
        self.json_handler.write_json(self.file_name)
        return book, 201
    
    def delete(self, id):
        """
        Deletes the record if exist and returns the data with response code 200 OK. 
        Otherwise 404 not found.
        """
        self.json_handler.read_json(self.file_name)

        try:
            self.json_handler.get_books_list().index(id)
            self.json_handler.delete_element(id)
            self.json_handler.write_json(self.file_name)

            return "{} is deleted.".format(id), 200
        except ValueError:
            return "Id {} does not exist".format(id), 404

