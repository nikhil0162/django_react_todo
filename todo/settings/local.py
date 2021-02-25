from django.conf import settings


if not settings.PRODUCTION_READY:
    from .base import *
    SECRET_KEY = '8f3gg$1*l(2%!p%rot2q9a4xb1!u8o78)$o9irc=$)63f42-rq'
    DEBUG = True
    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
