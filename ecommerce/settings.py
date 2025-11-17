




# Kwa project zingine kama hizi au mifumo mbalimbali ya 
# kusimamia biashara na shughuli zingine nitafute kwa mawasiliano haya
# phone: 0629712678
# Email: barackwilliam12@gmail.com
# Whatsaap: 0629712678

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#vw(03o=(9kbvg!&2d5i!2$_58x@_-3l4wujpow6(ym37jxnza'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecom',
    'pyuploadcare.dj',
    'widget_tweaks',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',       
        'USER': 'postgres.uhjyiagezazhquwxkpks',           
        'PASSWORD': 'NyumbaChap',    
        'HOST': 'aws-0-eu-north-1.pooler.supabase.com', 
        'PORT': '5432',              # Port ya PostgreSQL
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }




# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# UPLOADCARE = {
#     'pub_key': '7e9984d93874d32944be',
#     'secret': 'ff3a2603eff6cca1b577',
# }
# UPLOADCARE_PUBLIC_KEY = '7e9984d93874d32944be'


UPLOADCARE = {
    'pub_key': '5ff964c3b9a85a1e2697',
    'secret': '3842ddaed74fa5026064',
}




# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'from@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'xyz'  # Replace with your email password
EMAIL_RECEIVING_USER = ['to@gmail.com']  # Replace with the email where you receive messages

LOGIN_REDIRECT_URL = '/afterlogin'


# Static files storage (for Heroku)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'