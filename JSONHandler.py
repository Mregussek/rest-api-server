import json


class JSONHandler(object):
    def __init__(self, json_data=None):
        if json_data is not None:
            self.starting_books = json_data['books']
        else:
            self.starting_books = None

        self.json_data = json_data

    def read_json(self, file_name):
        with open(file_name, 'r') as f:
            self.json_data = json.load(f)

        return self.json_data

    def get_books_list(self):
        return self.json_data['books']

    def append_new_element(self, new_book):
        try:
            self.starting_books.append(new_book)
            self.json_data = {'books': self.starting_books}
            return True
        except:
            return False

    def write_json(self, file_name):
        try:
            with open(file_name, 'w') as f:
                json.dump(self.json_data, f)

            return True
        except:
            return False
