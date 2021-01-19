"""
Django settings for PyHyperspace project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from django.utils.translation import ugettext_lazy as _
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+n6+4x$6=y_mne9cz-ozi4q89i6timhdi^514p)@yrzcmyt)01'

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
    'ckeditor',
    'ckeditor_uploader',
    'constance',
    'constance.backends.database',
    'Content.apps.ContentConfig'
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

ROOT_URLCONF = 'PyHyperspace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Content.context_processors.show_system_content'
            ],
        },
    },
]

WSGI_APPLICATION = 'PyHyperspace.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGES = [
    ('en', _('English')),
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "templates/static"),
]

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

# CONSTANCE Settings
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
CONSTANCE_DATABASE_CACHE_BACKEND = 'default'

CONSTANCE_ADDITIONAL_FIELDS = {
    'yes_no_select': ['django.forms.fields.ChoiceField', {
        'widget': 'django.forms.Select',
        'choices': (
            ("yes", _('Yes')),
            ("no", _('No'))
        )
    }],
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_CONFIG = {
    'SITE_TITLE': ('My Blog', _('Title of this site!'), str),
    'SITE_DESCRIPTION': ('Blog Description', _('Description of this site!'), str),
    'SITE_FAVICON': ('default_favicon.png', _('Favicon of this site!'), 'image_field'),

    'GET_IN_TOUCH_TITLE': ('Get in touch', _('"Get in touch" title'), str),
    'GET_IN_TOUCH_DESCRIPTION': ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', _('"Get in touch" description text'), str),
    'GET_IN_TOUCH_EMAIL_ADDRESS': ('information@untitled.tld', _('"Get in touch" email address'), str),
    'GET_IN_TOUCH_PHONE': ('(000) 000-0000', _('"Get in touch" phone number'), str),
    'GET_IN_TOUCH_ADDRESS': ('1234 Somewhere Road #8254<br />Nashville, TN 00000-0000', _('"Get in touch" address'), str),

    'SOCIAL_NETWORKS_FACEBOOK_URL': ('#', _('Social Networks - Facebook'), str),
    'SOCIAL_NETWORKS_TWITTER_URL': ('#', _('Social Networks - Twitter'), str),
    'SOCIAL_NETWORKS_INSTAGRAM_URL': ('#', _('Social Networks - Instagram'), str),
    'SOCIAL_NETWORKS_GITHUB_URL': ('#', _('Social Networks - Github'), str),
    'SOCIAL_NETWORKS_LINKEDIN_URL': ('#', _('Social Networks - LinkedIn'), str),

    'SKILLS_TITLE': ('Get in touch', _('"Get in touch" title'), str),
    'SKILLS_DESCRIPTION': ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', _('"Get in touch" description text'), str),

}

CONSTANCE_CONFIG_FIELDSETS = {
    'General Options': (
        'SITE_TITLE',
        'SITE_DESCRIPTION',
        'SITE_FAVICON',
    ),
    '"Get in touch" Options': (
        'GET_IN_TOUCH_TITLE',
        'GET_IN_TOUCH_DESCRIPTION',
        'GET_IN_TOUCH_EMAIL_ADDRESS',
        'GET_IN_TOUCH_PHONE',
        'GET_IN_TOUCH_ADDRESS',
    ),
    '"Skills" Options': (
        'SKILLS_TITLE',
        'SKILLS_DESCRIPTION',
    ),
    '"Social Networks" Options': (
        'SOCIAL_NETWORKS_FACEBOOK_URL',
        'SOCIAL_NETWORKS_TWITTER_URL',
        'SOCIAL_NETWORKS_INSTAGRAM_URL',
        'SOCIAL_NETWORKS_GITHUB_URL',
        'SOCIAL_NETWORKS_LINKEDIN_URL',
    ),
}
# CONSTANCE Settings
