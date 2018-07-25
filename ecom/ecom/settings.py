"""
Django settings for ecom project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!a*36t)(zl&%$5l#ultl@6&tk2i2splr50w4*byw&jo1%fu+#g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookstore',
    'cart',
    'isbn_field',
    'orders',
    'localflavor',
    'parler',
    'payment',
    'paypal.standard.ipn',
    'paypal',
    'phonenumber_field',
    'promos',
    'rosetta',
    'redis',
    'users',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = (60 * 60)
CACHE_MIDDLEWARE_KEY_PREFIX = ''

ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecom.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Русский')),
)

LANGUAGE_CODE = 'en'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

LOGOUT_REDIRECT_URL = 'bookstore:book_list'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dev'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_prod')

# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Site's promo

SITE_NAME = 'My Bookstore'

META_KEYWORDS = 'Books, magazines'

META_DESCRIPTION = 'My Bookstore is an online supplier of books and magazines'

CART_SESSION_ID = 'cart'

# Phone number format
# https://github.com/stefanfoulis/django-phonenumber-field
PHONENUMBER_DB_FORMAT = 'INTERNATIONAL'

# Parler translation settings
# http://django-parler.readthedocs.io/en/latest/

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'ru'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

# PayPal integration
# https://django-paypal.readthedocs.io/en/stable/

PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = 'archeski.dk-facilitator@gmail.com'


# Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_CONNECT_RETRY = True


# Celery
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#general-settings

# CELERY_BROKER_URL = 'redis://localhost'
# CELERY_SEND_EVENTS=True
# CELERY_RESULT_BACKEND='redis'
# CELERY_REDIS_HOST='localhost'
# CELERY_REDIS_PORT=6379
# CELERY_REDIS_DB = 0
# CELERY_TASK_RESULT_EXPIRES = 10
# CELERY_ALWAYS_EAGER=False


# SMTP mailing
# https://docs.djangoproject.com/en/2.0/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'archeski.dk@gmail.com'
EMAIL_HOST_PASSWORD = 'antonYouSuckAtHacking2018'
DEFAULT_FROM_EMAIL = 'archeski.dk@gmail.com'
SERVER_EMAIL = 'archeski.dk@gmail.com'
DEFAULT_TO_EMAIL = 'archeski.dk@gmail.com'
