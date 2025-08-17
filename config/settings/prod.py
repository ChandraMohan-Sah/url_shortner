from .base import *
import dj_database_url
from decouple import config

DEBUG = False
ALLOWED_HOSTS = ['short.pythonanywhere.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database' /'db.sqlite3',
    }
}