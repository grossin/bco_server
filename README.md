# bco_server

To run the server:
1) cd bco_server
2) python manage.py runserver

To test the API:
1) download httpie
2) open new terminal
3) run sample GET command: http http://127.0.0.1:8000/users/
   
   sample output:
   
    HTTP/1.0 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Length: 308
    Content-Type: application/json
    Date: Fri, 14 Apr 2017 00:26:20 GMT
    Server: WSGIServer/0.2 CPython/3.6.1
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN

    [
        {
            "dob": "1986-08-18",
            "email": "georgerossin@gmail.com",
            "first_name": "george",
            "id": 1,
            "last_name": "rossin",
            "password": "password123",
            "username": "grossin"
        },
        {
            "dob": "1988-01-01",
            "email": "ryan.fraser.2018@anderson.ucla.edu",
            "first_name": "ryan",
            "id": 2,
            "last_name": "fraser",
            "password": "fanfolio",
            "username": "rfraser"
        }
    ]
