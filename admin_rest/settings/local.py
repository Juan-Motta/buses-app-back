from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2iom80lpupuor',
        'USER': 'zfxwbvqwaiytzn',
        'PASSWORD': '435e1656174d73d82c6f48cfe0acb7486dd34d875bbaf4b1a6e010b08a2e4065',
        'HOST': 'ec2-54-204-148-110.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
