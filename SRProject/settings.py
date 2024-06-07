"""
Django settings for SRProject project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#print(BASE_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR,'Templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c0#o=fx5--w%!2v4xvq=(i5^a=&h*9-lv9*v$^8a(oqmpm-^6a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['zoness.pythonanywhere.com','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_select2', # This package provides enhanced select boxes that support search functionality in templates 
    'SR_Plant_I',
    'Packing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Packing.middleware.CurrentUserMiddleware', # updated for User Edit Log
    #'SRProject.middleware.CustomeMiddleware'
]

ROOT_URLCONF = 'SRProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SRProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
from decouple import Config, Csv


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'SRProject', 
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'HOST': 'localhost', 
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# # Replace the DATABASES section of your settings.py with this
# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'SRProject',
#     'USER': 'SRProject_owner',
#     'PASSWORD': '6nyh1MHsUrab',
#     'HOST': 'ep-cool-sea-a5cdjbtt.us-east-2.aws.neon.tech',
#     'PORT':  '5432',
#     'OPTIONS': {
#       'sslmode': 'require',
#     },
#   }
# }

# # Add these at the top of your settings.py
# from os import getenv
# from dotenv import load_dotenv

# # Replace the DATABASES section of your settings.py with this
# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': getenv('PGDATABASE'),
#     'USER': getenv('PGUSER'),
#     'PASSWORD': getenv('PGPASSWORD'),
#     'HOST': getenv('PGHOST'),
#     'PORT': getenv('PGPORT', 5432),
#     'OPTIONS': {
#       'sslmode': 'require',
#     },
#   }
# }
# create below code to dotenv for safe in above code
# PGHOST='ep-cool-sea-a5cdjbtt.us-east-2.aws.neon.tech'
# PGDATABASE='SRProject'
# PGUSER='SRProject_owner'
# PGPASSWORD='6nyh1MHsUrab'




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'

#AUTH_USER_MODEL = 'SR_Plant_I.CustomUser'

# Security settings
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True

# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600  # Two weeks, adjust as needed
