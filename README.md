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

Thankfully to this line user is able to run server on docker container:

```python
rest_app.run(host='0.0.0.0', debug=True, port=8080)
```

*host='0.0.0.0'* it makes app to run on all your machines IP addresses. By default it runs on localhost and you are not allowed to request anything.

## Usage

### Python 

Install requirenmnents for this project:

```bash
pip3 install -r requirements.txt
```

and run server:

```bash
python server.py
```

You should get sth like this:

```bash
python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 119-369-464
 ```

### Docker

For this I have prepared *Dockerfile*. Firstly you have to build application:

```bash
sudo docker build server .
```

and then run it:

```bash
sudo docker run -p 8080:8080 server
```

 ## REST API requests

 I am using Postman for this, but there is another way to do this. You need to install curl:

 ```bash
sudo apt install curl
 ```

 and for instance GET request:

 ```bash
curl -XGET http://127.0.0.1:8080/books

curl -XGET http://127.0.0.1:8080/books/02
 ```

Also POST method:

 ```bash
curl -XPOST http://127.0.0.1:8080/books -H "Content-Type: application/json"  --data '{ "id": "04", "title": "New Book", "author": "Mateusz Rzeczyca" }'
```

## Author

Mateusz Rzeczyca

[info@mateuszrzeczyca.pl](mailto:info@mateuszrzeczyca.pl)

Cracow, Poland

26.02.2020