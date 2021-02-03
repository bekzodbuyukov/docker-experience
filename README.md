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

After creating Dockerfile put in it content below:

``# Pull base image
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
COPY . /django_project/``
