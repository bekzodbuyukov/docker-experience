import environ


# making env
env = environ.Env()

# reading .env file
environ.Env.read_env('../.env')

# getting values
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
