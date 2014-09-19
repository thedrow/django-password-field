#!/usr/bin/env python
# coding: utf-8
USE_TZ = True

SECRET_KEY = 'secretkey'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': ':memory:'
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'tests.unit.support'
)

PASSWORD_HASHERS = ('django_plainpasswordhasher.PlainPasswordHasher', )