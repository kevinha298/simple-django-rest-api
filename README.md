# simple-django-rest-api
A simple rest api using django and postgres on docker containers.

1) Open git bash from local repository directory

2) Clone project from remote git to local repositorydirectory:
git clone https://github.com/kevinha298/django-postgres-docker.git

3) Open project in vs code:
code .

4) Create djangoapp folder at the root of the project to store Django files

5) Create pgdb folder at the root of the project to store Postgresql data

6) Build a docker image of the containers for the first time and create a Django app:
docker-compose run --rm app sh -c "django-admin startproject MainApp ."

7) Start up docker containers from the new built docker image above:
docker-compose up

8) Test django default site:
http://127.0.0.1:8000/

9) Open another terminal session for the following instructions (get into the app service of the django_app container to create a new app "api"):
docker-compose exec app sh
python manage.py startapp api
exit

10) Stop docker containers to make changes to the containers' content:
docker-compose down

11) Delete db.sqlite3 file in the djangoapp folder

12) In the ./djangoapp/MainApp/settings.py file do the following on the top:
import os

13) In the ./djangoapp/MainApp/settings.py file update "SECRET_KEY" variable as following:
SECRET_KEY = os.environ.get('SECRET_KEY')

14) In the ./djangoapp/MainApp/settings.py file update "DEBUG" variable as following:
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

15) In the ./djangoapp/MainApp/settings.py file add "ALLOWED_HOSTS" variable as following:
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)

16) In the "INSTALLED_APPS" section of the ./djangoapp/MainApp/settings.py file, add the following line,:
'rest_framework',
'api',

17) Replace "DATABASES" section in the ./djangoapp/MainApp/settings.py file with the following:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

18) Migrate django objects and connect to postgresql database: 
docker-compose run app python manage.py migrate

19) Start up docker containers:
docker-compose up

20) Add class Employee in the model.py file in the api folder:
class Employee(models.Model):
    fullName = models.CharField(max_length=100)
    empCode = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

21) Open another terminal session for the following instructions (get into the app service of the django_app container to create a migration file for model class just created above and then migrate the model to the database):
docker-compose exec app sh
python manage.py makemigrations api  
python manage.py migrate









20) Once inside the app service of the django_app container, create a super user and enter username, email address, and password
python manage.py createsuperuser


21) Go to admin site to test:
http://127.0.0.1:8000/admin

22) Enter username and password for admin to test

23) To rebuild image created above after making any change to the containers in the docker-compose.yml file:
docker-compose build

