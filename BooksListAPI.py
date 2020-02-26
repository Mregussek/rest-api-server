# Written by Mateusz Rzeczyca

from flask_restful import Resource, reqparse
import json


class BooksListAPI(Resource):
    def __init__(self):
        with open('books.json', 'r') as f:
            json_data = json.load(f)

        self.books = json_data["books"]

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str, required=True,
                                 help='No book title provided', location='json')
        self.parser.add_argument("edition", type=str, default='Not given',
                                 location = 'json')
        self.parser.add_argument("author", type=str, required=True,
                                 help='No book author provided', location='json')

    def get(self):
        if self.books is not None:
            return self.books, 200
        else:
            return "Books not found", 404

    def post(self):
        pass
