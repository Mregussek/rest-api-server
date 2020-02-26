# REST API server

Repository created in order to learn REST API capabilities and write my own server to see how it look likes. Client app is [Postman](https://www.postman.com/), which I use to query specific data.

## Explanation

I define two URLs: for the list of books and for an individual book.

```python
api.add_resource(BooksListAPI, "/books", endpoint="books")
api.add_resource(BooksAPI, "/books/<string:id>", endpoint="book")
```

In the BooksListAPI resource the POST method is the only one the receives arguments. The title and author arguments are required here, so I included an error message that Flask-RESTful will send as a response to the client when the field is missing.

```python
self.parser.add_argument("title", type=str, required=True,
                            help='No book title provided', location='json')
self.parser.add_argument("edition", type=str, default='Not given',
                            location = 'json')
self.parser.add_argument("author", type=str, required=True,
                            help='No book author provided', location='json')
```

One interesting aspect of the *RequestParser* class is that by default it looks for fields in request.values, so the location optional argument must be set to indicate that the fields are coming in *request.json*.