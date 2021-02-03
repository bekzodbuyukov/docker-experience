# docker-experience
To get experience of using Docker

## Setting virtual environment
How to create new virtual enivornment with Django:

`$ pipenv install django`

As a result you should get new files: **Pipfile** and **Pipfile.lock**

To activate created virtual environment:

`$ pipenv shell`

**P.S.**: If something went wrong on a Linux, just try this commands with `sudo`.

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

After creating Dockerfile put in it the content below:

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

To create docker-composer.yml file:

`$ touch docker-composer.yml`

docker-compose.yml file should contain the following code:

```
version: '3.9' # recent version of Docker Compose

services: # services we want to have running within our Docker host
  web:
    build: . # Dockerfile directory (. - directory, where docker-compose.yml is located)
    command: python /django_project/manage.py runserver 127.0.0.1:8000 # command to start up the local server
    volumes: # for mounting automatically sync the Docker filesystem with our local computer's filesystem
      - .:/django_project
    ports: # ports to expose within Docker
      - 8000:8000
```

To run Docker container:

`$ docker-compose up`
