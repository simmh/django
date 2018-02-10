# settings/local.py
# settings/dev.py
from .base import *
DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DATABASES = {
#   "default": {
#     "ENGINE": "django.db.backends.postgresql _ psycopg2",
#     "NAME": "twoscoops",
#     "USER": "",
#     "PASSWORD": "",
#     "HOST": "localhost",
#     "PORT": "",
#   }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': (BASE_DIR.child("db.sqlite3")),
    }
}

# INSTALLED _ APPS += ("debug_toolbar", )
INSTALLED_APPS += ()
