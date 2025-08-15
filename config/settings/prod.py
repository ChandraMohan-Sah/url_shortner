from .base import *
import dj_database_url
from decouple import config

DEBUG = True
ALLOWED_HOSTS = []


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('NAME'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#         'HOST': config('HOST'),
#         'PORT': config('PORT', default='5432'),
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        default=config("DATABASE_URL"),  # Provided by Railway
        conn_max_age=600,
        ssl_require=True
    )
}