#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import CharField
from django.utils import six
from django.utils.encoding import smart_text


class PasswordFieldDescriptor(object):
    def __init__(self):
        self.value = None

    def __eq__(self, other):
        def setter(raw_password):
            self.value = make_password(raw_password)

        return check_password(other, self.value, setter=setter)

    def __set__(self, instance, value):
        if instance.password.value != value:
            self.value = make_password(value)

    def __str__(self):
        return smart_text(self.value)


class PasswordField(CharField):
    def __init__(self, *args, **kwargs):
        max_length = kwargs.pop('max_length', 512)

        super(PasswordField, self).__init__(max_length=max_length, *args, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super(PasswordField, self).contribute_to_class(cls, name, **kwargs)

        setattr(cls, name, PasswordFieldDescriptor())

    def to_python(self, value):
        if isinstance(value, six.string_types) or value is None:
            return value
        return smart_text(value.value)
