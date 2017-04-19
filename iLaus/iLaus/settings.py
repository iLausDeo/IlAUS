"""
Django settings for iLaus project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n+mbeybwihwh^%bv(o89m+6#9ia7!^^t%^6irbk5#euuk79bvh'

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
    'rest_framework',
    'index',
    'ilaus_message',
    'users',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
]

ROOT_URLCONF = 'iLaus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'iLaus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

ILAUS_DB_NAME = os.environ.get('ILAUS_DB_NAME', 'king_ilaus')
ILAUS_DB_USER = os.environ.get('ILAUS_DB_USER', 'root')
ILAUS_DB_PASSWORD = os.environ.get('ILAUS_DB_PASSWORD', '123456')
ILAUS_DB_HOST = os.environ.get('ILAUS_DB_HOST', '192.168.1.119')
ILAUS_DB_PORT = os.environ.get('ILAUS_DB_PORT', '5432')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ILAUS_DB_NAME,
        'USER': ILAUS_DB_USER,
        'PASSWORD': ILAUS_DB_PASSWORD,
        'HOST': ILAUS_DB_HOST,
        'PORT': ILAUS_DB_PORT,
    }
}


# Use Django's standard `django.contrib.auth` permissions,
# or allow read-only access for unauthenticated users.

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'PAGINATE_BY': 10
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN'

# TIME_ZONE = 'UTC'
# TIME_ZONE = 'Etc/GMT-8'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# some self setting by os.environ



# aliyun 账号
ALIYUN_ACCESS_KEY_ID = os.environ.get("ALIYUN_ACCESS_KEY_ID","")
ALIYUN_ACCESS_KEY_SECRET = os.environ.get("ALIYUN_ACCESS_KEY_SECRET","")
# 在部署之前使用外网endpoint
ALIYUN_SMS_OUTNET_ENDPOINT = ""
ALIYUN_SMS_INNET_ENDPOINT = ""
ALIYUN_SMS_VPC_ENDPOINT = ""
ALIYUN_SMS_USE_ENDPOINT = ALIYUN_SMS_OUTNET_ENDPOINT

ALIYUN_SMS_REGIONID = os.environ.get("ALIYUN_SMS_REGIONID","cn-hangzhou")




