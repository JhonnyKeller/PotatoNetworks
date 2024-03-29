"""
Django settings for myPortfolio project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'
MEDIA_DIR = BASE_DIR / 'media'
STATIC_DIR = BASE_DIR / 'static'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(config('DJANGO_SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = str(config('DEBUG')) == "1" # 1 == "True"


ALLOWED_HOSTS = [str(config('ALLOWED_HOSTS')),'www.potatonetworks.com','potatonetworks.com','127.0.0.1',]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "phonenumber_field",
    'crispy_forms',
    'users',
    'resume',
    'main',
    'services',
    'portfolioAppTwo',
    'contact',
    'captcha',
    'colorfield',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myPortfolio.urls'

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
                'main.context_processors.get_navbar',
                'services.context_processors.get_servicespages',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = ['users.backends.EmailBackend']

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')
SILENCED_SYSTEM_CHECKS = 'captcha.recaptcha_test_key_error'

WSGI_APPLICATION = 'myPortfolio.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap4'


                   # Databases
if DEBUG:
    DATABASES = {
        'default' : {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'potatodata',
            'USER': 'postgres',
            'PASSWORD': str(config('DBOFDATAPASS')),
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
            'default' : {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'portfoliodb',
            'USER': 'mia',
            'PASSWORD': str(config('DBONDATAPASS')),
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# MEDIA_DIR

MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

#Email Section
ADMINS = (
    ('Jhonny Keller', 'jhonnykellerdev@gmail.com'),
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jhonnykellerdev@gmail.com'
EMAIL_HOST_PASSWORD = str(config('EMAIL_HOST_PASSWORD'))

PASSWORD_RESET_TIMEOUT = 14400

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'media')
STATIC_ROOT = os.path.join(BASE_DIR , 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
