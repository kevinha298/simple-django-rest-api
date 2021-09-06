# simple-django-rest-api
A simple rest api using django and postgres on docker containers.

1) Open git bash from local repository directory

2) Clone project from remote git to local repositorydirectory:
git clone git@github.com:kevinha298/simple-django-rest-api.git

3) Open project in vs code:
code .

4) Create pgdb folder at the root of the project to store Postgresql data 

5) Open a terminal session in vs code for the following instructions:

docker-compose build

docker-compose run app python manage.py migrate

docker-compose up

6) Test API calls:

POST = create/insert/add
GET = retrieve/fetch
PUT = update/edit
DELETE = remove/delete

GET: http://127.0.0.1:8000/api/employee/2
POST: http://127.0.0.1:8000/api/employee/2
PUT: http://127.0.0.1:8000/api/employee/2/
DELETE: http://127.0.0.1:8000/api/employee/2

