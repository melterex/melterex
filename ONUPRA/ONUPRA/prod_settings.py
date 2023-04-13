from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-48cu=1(5ln)ydmpn-%%e)0@*u+wel*tmfhdn59uss&6^_1$gj7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['onupra.ru', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = [
    'https://onupra.ru', 'http://127.0.0.1:8000']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onupra',
        'USER': 'dbuser',
        'PASSWORD': 'gaysex32',
        'HOST': 'localhost',
        'PORT': '8000'
    }
}

STATICFILES_DIRS = [
    BASE_DIR / "main/static/",
]