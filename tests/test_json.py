import unittest
import sys
sys.path.append("..")

from JSONHandler import JSONHandler


class JsonTestCase(unittest.TestCase):
    maxDiff = None

    def __init__(self, *args, **kwargs):
        super(JsonTestCase, self).__init__(*args, **kwargs)
        self.json_data = {
            "books": [
                {
                    "id": "01",
                    "language": "A Tour of C++",
                    "edition": "second",
                    "author": "Byarne Stroustrup"
                },
                {
                    "id": "02",
                    "language": "Python3",
                    "edition": "first",
                    "author": "Zed E. Shaw"
                },
                {
                    "id": "03",
                    "language": "Design Patterns",
                    "edition": "first",
                    "author": "Gang of Four"
                }
            ]
        }

        self.new_book = {
            "id": "04",
            "language": "New book",
            "edition": "asd",
            "author": "Mateusz Rzeczyca"
        }

        self.json_data_deleted = {
            "books": [
                {
                    "id": "01",
                    "language": "A Tour of C++",
                    "edition": "second",
                    "author": "Byarne Stroustrup"
                },
                {
                    "id": "02",
                    "language": "Python3",
                    "edition": "first",
                    "author": "Zed E. Shaw"
                }
            ]
        }

        self.id_to_delete = "03"
        self.file_name = 'test_books.json'
        self.new_file_name = 'new_test_books.json'

    def test_reading_json(self):
        json_handler = JSONHandler()
        self.assertEqual(json_handler.read_json(self.file_name), self.json_data)
        self.assertEqual(json_handler.get_books_list(), self.json_data['books'])

    def test_appending_new_book_json(self):
        json_handler = JSONHandler(self.json_data)
        self.assertTrue(json_handler.append_new_element(self.new_book))
        self.json_data['books'].append(self.new_book)
        self.assertEqual(self.json_data['books'], json_handler.get_books_list())

    def test_reading_new_book(self):
        json_handler = JSONHandler(self.json_data)
        self.assertTrue(json_handler.append_new_element(self.new_book))
        self.assertTrue(json_handler.write_json(self.new_file_name))
        self.assertEqual(self.json_data, json_handler.read_json(self.new_file_name))

    def test_deleting_book(self):
        json_handler = JSONHandler(self.json_data)
        self.json_data['books'].pop()
        self.assertTrue(json_handler.delete_element(self.id_to_delete))
        self.assertEqual(self.json_data_deleted['books'], json_handler.get_books_list())


if __name__ == '__main__':
    unittest.main()
