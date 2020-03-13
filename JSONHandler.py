import json


class JSONHandler(object):
    def __init__(self, json_data=None):
        if json_data is not None:
            self.books = json_data['books']
        else:
            self.books = None

        self.json_data = json_data

    def read_json(self, file_name):
        try:
            with open(file_name, 'r') as f:
                self.json_data = json.load(f)

            return True
        except:
            return False

    def write_json(self, file_name, given_json_data=None):
        try:
            with open(file_name, 'w') as f:
                if given_json_data is not None:
                    json.dump(given_json_data, f)
                else:
                    json.dump(self.json_data, f)

            return True
        except:
            return False

    def append_new_element(self, new_book):
        try:
            self.books.append(new_book)
            self.json_data = {'books': self.books}

            return True
        except:
            return False

    def put_element(self, book_to_put):
        try:
            for book in self.get_books_list():
                if book['id'] == book_to_put["id"]:
                    book["title"] = book_to_put["title"]
                    book["edition"] = book_to_put["edition"]
                    book["author"] = book_to_put["author"]

            return True
        except:
            return False

    def delete_element(self, id):
        try:
            books = [book for book in self.get_books_list() if book["id"] != id]
            self.books = books
            self.json_data = {'books': self.books}

            return True
        except:
            return False

    def get_json_data(self):
        return self.json_data

    def get_books_list(self):
        return self.json_data['books']
