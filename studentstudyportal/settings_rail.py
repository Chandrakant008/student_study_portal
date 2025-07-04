from studentstudyportal.settings import *
import os
from decouple import config, Csv

# Secret key for Django
SECRET_KEY = config('SECRET_KEY')

# Turn off debug mode in production
DEBUG = config('DEBUG', default=False, cast=bool)

# Correct usage: fetch ALLOWED_HOSTS as a comma-separated list
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Static files (for deployment)
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # for development
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Add WhiteNoise middleware to serve static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add here
    ...
]