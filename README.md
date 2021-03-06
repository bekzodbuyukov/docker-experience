# docker-experience
To get an experience of using Docker

General pattern (algorithm):
1. [create a virtual environment locally and install Django](#setting-virtual-environment)
2. [create a new project](#creating-django-project)
3. [exit the virtual environment](#setting-virtual-environment)
4. [write a Dockerfile and then build the initial image](#setting-docker)
5. [write a docker-compose.yml file and run the container with docker-compose up](#setting-docker)

## Setting virtual environment
To create new virtual environment:

```bash
$ pipenv shell
```

As a result you should get new files: **Pipfile** and **Pipfile.lock**

If you got an error:

```bash
ModuleNotFoundError: No module named 'virtualenv.seed.embed.via_app_data'
...
```

look [there](https://stackoverflow.com/a/65845074/15165438) for solution.

To install Django:

```bash
$ pipenv install django
```

To activate created virtual environment:

```bash
$ pipenv shell
```

To stop virtual environment:

```bash
(venv) $ exit
```

## Creating Django project
In activated environment's shell enter:

```bash
(venv) $ django-admin startproject django_project
```

Use **migrate** to initialize the database:

```bash
(venv) ../django_project $ python manage.py migrate
```

Command **runserver** to start local web server:

```bash
(venv) ../django_project $ python manage.py runserver
```

Creating specific app, named pages:

```bash
(venv) ../django_project $ python manage.py startapp pages
```

**P.S.**: Don't forget to include created app in **django_project/settings.py** file in list **INSTALLED_APPS**.

## Setting Docker
Creating docker file:

```bash
$ touch Dockerfile
```

After creating Dockerfile (image instructions' file) put in it the content below:

```dockerfile
# Pull base image
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

```bash
$ docker build .
```

To create **docker-compose.yml** file:

```bash
$ touch docker-compose.yml
```

**docker-compose.yml** file (to control how to run the container) should contain the following code:

```yaml
version: '3.8' # recent version of Docker Compose

# services we want to have running within our Docker host
services:
  web:
    # Dockerfile directory (. - directory, where docker-compose.yml is located)
    build: .
    # command to start up the local server
    command: python django_project/manage.py runserver 0.0.0.0:8000
    # for mounting automatically sync the Docker filesystem
    # with our local computer's filesystem
    volumes:
      - .:/django_project
    # ports to expose within Docker
    ports:
      - 8000:8000
```

To run Docker container (use `-d` or `-detach` flag if you want to run in detached mode):

```bash
$ docker-compose up
```

**P.S.**: When software packages are updated, you should run command above with flag `--build`, you will force Docker to build a new image. By default, Docker looks for a local cached copy of software to improve performance.

To stop the Docker container use hotkey in terminal:

`Control+C`

To stop Docker container at all:

```bash
$ docker-compose down
```

## Additional information
If we preface traditional commands with `docker-compose exec [service]` like:

```bash
$ docker-compose exec web python django_project/manage.py createsuperuser
```

we can run commands through Docker.

**P.S.:** Each file change within Docker will be automatically synced/copied over into a file on our local computer. 

> Using book **Django for Professionals** by _William S. Vincent_
