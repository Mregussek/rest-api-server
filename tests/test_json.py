import unittest
import sys
sys.path.append("..")

import json
from JSONHandler import JSONHandler


class JsonTestCase(unittest.TestCase):
    maxDiff = None

    def test_reading_json(self):
        json_data = {
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

        good_data = json.dumps(json_data, ensure_ascii=False)
        json_handler = JSONHandler()
        test_data = json_handler.read_json('../books.json')
        test_data = json.dumps(test_data, ensure_ascii=False)
        self.assertEqual(test_data, good_data)


if __name__ == '__main__':
    unittest.main()