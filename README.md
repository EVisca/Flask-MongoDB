**Python CRUD with Flask and MongoDB **

This simple app was made following this guide for learning whenever I was in doubt about it. I hope it may be as useful to you as it was for me: https://www.youtube.com/watch?v=o8jK5enu4L4 <br />

## Local server and Database

MongoClient set to run a local server and MongoDB for the database

## Setup and Requests

Python, MongoDB are required to be installed prior to run this simple code. <br />
Flask Install: pip install flask <br />

For usage of the routes made for the CRUD protocol, Postman was used to send the request and also
to create/read/update/delete deta from the DB, using the listed routes and https (There may be some stuff needed to install directly with the terminal, but don't recall anythinh else at this moment). <br />

## Run the Code

Just run in your terminal at the mongo dir: cd Scripts => .\activate <br />
Then, it should show your path as: (mongo) PS C:\flask\mongo\Scripts> (or something similar). With this set, just insert the command "py server.py" and bam, the local server is running in the port of your choice. <br />

As a side note, previously doing some other codes with XAMPP, for some reason "localhost" in my machine was already taken at the time I made this. Using the regular  http://127.0.0.1:(port) did the trick instead, also for the requests with Postman.
