import unittest
import sys
sys.path.append("..")

from JSONHandler import JSONHandler


class JsonTestCase(unittest.TestCase):
    maxDiff = None

    def test_reading_json(self):
        json_data = {
            "books": [
                {
                    "id": "01",
                    "title": "A Tour of C++",
                    "edition": "second",
                    "author": "Byarne Stroustrup"
                },
                {
                    "id": "02",
                    "title": "Python3",
                    "edition": "first",
                    "author": "Zed E. Shaw"
                },
                {
                    "id": "03",
                    "title": "Design Patterns",
                    "edition": "first",
                    "author": "Gang of Four"
                }
            ]
        }
        file_name = 'test_books.json'

        json_handler = JSONHandler()
        self.assertTrue(json_handler.read_json(file_name))
        self.assertEqual(json_handler.get_json_data(), json_data)
        self.assertEqual(json_handler.get_books_list(), json_data['books'])

    def test_appending_new_book_json(self):
        json_data = {
            "books": [
                {
                    "id": "01",
                    "title": "A Tour of C++",
                    "edition": "second",
                    "author": "Byarne Stroustrup"
                },
                {
                    "id": "02",
                    "title": "Python3",
                    "edition": "first",
                    "author": "Zed E. Shaw"
                },
                {
                    "id": "03",
                    "title": "Design Patterns",
                    "edition": "first",
                    "author": "Gang of Four"
                }
            ]
        }
        new_book = {
            "id": "04",
            "title": "New book",
            "edition": "asd",
            "author": "Mateusz Rzeczyca"
        }

        json_handler = JSONHandler(json_data)
        self.assertTrue(json_handler.append_new_element(new_book))
        json_data['books'].append(new_book)
        self.assertEqual(json_data['books'], json_handler.get_books_list())

    def test_reading_new_book(self):
        json_data = {
            "books": [
                {
                    "id": "01",
                    "title": "A Tour of C++",
                    "edition": "second",
                    "author": "Byarne Stroustrup"
                },
                {
                    "id": "02",
                    "title": "Python3",
                    "edition": "first",
                    "author": "Zed E. Shaw"
                },
                {
                    "id": "03",
                    "title": "Design Patterns",
                    "edition": "first",
                    "author": "Gang of Four"
                }
            ]
        }
        new_book = {
            "id": "04",
            "title": "New book",
            "edition": "asd",
            "author": "Mateusz Rzeczyca"
        }
        new_file_name = 'test_new_books.json'

        json_handler = JSONHandler(json_data)
        self.assertTrue(json_handler.append_new_element(new_book))
        self.assertTrue(json_handler.write_json(new_file_name))
        self.assertTrue(json_handler.read_json(new_file_name))
        self.assertEqual(json_data, json_handler.get_json_data())

    def test_deleting_book(self):
        json_data_deleted = {
            "books": [
                {
                    "id": "01",
                    "title": "A Tour of C++",
                    "edition": "second",
                    "author": "Byarne Stroustrup"
                },
                {
                    "id": "02",
                    "title": "Python3",
                    "edition": "first",
                    "author": "Zed E. Shaw"
                }
            ]
        }
        file_name = 'test_books.json'
        id_to_delete = "03"

        json_handler = JSONHandler()
        self.assertTrue(json_handler.read_json(file_name))
        self.assertTrue(json_handler.delete_element(id_to_delete))
        self.assertEqual(json_data_deleted, json_handler.get_json_data())
        self.assertEqual(json_data_deleted['books'], json_handler.get_books_list())

    def test_putting_element(self):
        json_data_put = {
            "books": [
                {
                    "id": "01",
                    "title": "A Tour of C++",
                    "edition": "second",
                    "author": "Byarne Stroustrup"
                },
                {
                    "id": "02",
                    "title": "New book",
                    "edition": "asd",
                    "author": "Mateusz Rzeczyca"
                },
                {
                    "id": "03",
                    "title": "Design Patterns",
                    "edition": "first",
                    "author": "Gang of Four"
                }
            ]
        }
        file_name = 'test_books.json'
        file_name_to_put = 'test_put_books.json'
        book_to_put = {
                    "id": "02",
                    "title": "New book",
                    "edition": "asd",
                    "author": "Mateusz Rzeczyca"
                }

        json_handler = JSONHandler()
        self.assertTrue(json_handler.read_json(file_name))
        self.assertTrue(json_handler.put_element(book_to_put))
        self.assertEqual(json_data_put, json_handler.get_json_data())
        self.assertEqual(json_data_put['books'], json_handler.get_books_list())
        self.assertTrue(json_handler.write_json(file_name_to_put))


if __name__ == '__main__':
    unittest.main()
