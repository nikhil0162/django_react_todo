from django.conf import settings


if settings.PRODUCTION_READY:
    from .base import *
    SECRET_KEY = '8f3gg$1*l(2%!p%rot2q9a4xb1!u8o78)$o9irc=$)63f42-rq'
    DEBUG = True
    ALLOWED_HOSTS = []

    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

    DATABASES = {

        'default': {

            'ENGINE': 'django.db.backends.postgresql_psycopg2',

            'NAME': 'todo_db',

            'USER': 'todo_db_username',

            'PASSWORD': 'todo_db_password',

            'HOST': 'localhost',

            'PORT': '',

        }

    }
