import json


class JSONHandler(object):
    def __init__(self):
        self.starting_books = None

    def read_json(self, file_name):
        with open(file_name, 'r') as f:
            json_data = json.load(f)

        self.starting_books = json_data['books']
        return self.starting_books

    def write_json(self, file_name, new_book):
        self.starting_books.append(new_book)
        data = {'books': self.starting_books}

        with open(file_name, 'w') as f:
            json.dump(data, f)
