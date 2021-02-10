import environ


# # making env
env = environ.Env()

# reading .env file
env.read_env()

#  # getting values
DEBUG = env('DEBUG', default=True)
SECRET_KEY = env('SECRET_KEY', default="NEED SECRET KEY")
