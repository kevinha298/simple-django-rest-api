# simple-django-rest-api
A simple rest api using django and postgres on docker containers.

1) Open git bash from local repository directory

2) Clone project from remote git to local repositorydirectory:
git clone git@github.com:kevinha298/simple-django-rest-api.git

3) Open project in vs code:
code .

4) Open first terminal session in vs code to build container image:
docker-compose up

5) Open second terminal session in vs code to migrate Django models to Postgresql database:
docker-compose run app python manage.py migrate

6) On the second terminal session in vs code, build image containers and stop the containers:
docker-compose build
docker-compose down

7) On the second terminal session in vs code, start the containers:
docker-compose up

8) Test API calls:

POST = create/insert/add
GET = retrieve/fetch
PUT = update/edit
DELETE = remove/delete

GET: http://127.0.0.1:8000/api/employee/2
POST: http://127.0.0.1:8000/api/employee/2
PUT: http://127.0.0.1:8000/api/employee/2/
DELETE: http://127.0.0.1:8000/api/employee/2

