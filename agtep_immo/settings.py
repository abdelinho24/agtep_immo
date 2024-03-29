"""
Django settings for agtep_immo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'du2u_(p^(0%gw8^f^^&2+v(zex^y&jj*cp$+x7&dvzsh5_i15_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'presentation'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'agtep_immo.urls'

WSGI_APPLICATION = 'agtep_immo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'bello_agtep_db',
       'USER': 'bello',
       'PASSWORD': 'olivia',
       'HOST': ' postgresql1.alwaysdata.com',
       'PORT': '5432',
       'TEST_MIRROR': 'default',
   },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
  "/home/agtep_immo/presentation/templates/",
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#if DEBUG:
STATIC_ROOT = '/home/agtep_immo/public/static/'
#else:
  # STATIC_ROOT = 'home/bello/www/agtep_immo/public/static/'


STATIC_URL = '/static/' if DEBUG else 'http://www.agtep-immo.com/static/'

#ROOT_URLCONF = 'agtep_immo.urls'

#STATICFILES_DIRS = (
 # "/home/agtep_immo/presentation/static",
#)





