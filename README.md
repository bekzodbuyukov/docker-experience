# docker-experience
To get an experience of using Docker

General pattern (algorithm):
1. create a virtual environment locally and install Django
2. create a new project
3. exit the virtual environment
4. write a Dockerfile and then build the initial image
5. write a docker-compose.yml file and run the container with docker-compose up

## Setting virtual environment
To create new virtual environment:

`$ pipenv shell`

As a result you should get new files: **Pipfile** and **Pipfile.lock**

If you got an error:

```
ModuleNotFoundError: No module named 'virtualenv.seed.embed.via_app_data'
...
```

look [there](https://stackoverflow.com/a/65845074/15165438) for problem solution.

To install Django:

`$ pipenv install django`

To activate created virtual environment:

`$ pipenv shell`

To stop virtual environment:

`(venv) $ exit `

## Creating Django project
In activated environment's shell enter:

`(venv) $ django-admin startproject django_project`

Use **migrate** to initialize the database:

`(venv) $ python manage.py migrate`

Command **runserver** to start local web server:

`(venv) $ python manage.py runserver`

Creating specific app, named pages:

`(venv) $ python manage.py startapp pages`

**P.S.**: Don't forget to include created app in django_project/settings.py file in list **INSTALLED_APPS**.

## Setting Docker
Creating docker file:

`$ touch Dockerfile`

After creating Dockerfile (image instructions' file) put in it the content below:

```# Pull base image
FROM python:3.8.5

# Set environment variables
# Python will not try to write .pyc files which we do not desire
ENV PYTHONDONTWRITEBYTECODE 1
# ensures our console output looks familiar 
# and is not buffered by Docker, which we also don’t want
ENV PYHTONUNBUFFERED 1

# Set work directory
WORKDIR /django_project

# Install dependencies
COPY Pipfile Pipfile.lock /django_project/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /django_project/
```

Building image:

`$ docker build .`

To create docker-compose.yml file:

`$ touch docker-compose.yml`

docker-compose.yml file (to control how to run the container) should contain the following code:

```
version: '3.8' # recent version of Docker Compose

# services we want to have running within our Docker host
services:
  web:
    # Dockerfile directory (. - directory, where docker-compose.yml is located)
    build: .
    # command to start up the local server
    command: python django_project/manage.py runserver 0.0.0.0:8000
    # for mounting automatically sync the Docker filesystem with our local computer's filesystem
    volumes:
      - .:/django_project
    # ports to expose within Docker
    ports:
      - 8000:8000
```

To run Docker container (use -d flag if you want to run in detached mode):

`$ docker-compose up`

To stop the Docker container use hotkey in terminal:

`Control+C`

To stop Docker container at all:

`$ docker-compose down`

## Additional information
If we preface traditional commands with `docker-compose exec [service]` like:

`$ docker-compose exec web python manage.py createsuperuser`

we can run commands through Docker.

**P.S.:** Each file change within Docker will be automatically synced/copied over into a file on our local computer. 

> Using book **Django for Professionals** by _William S. Vincent_
