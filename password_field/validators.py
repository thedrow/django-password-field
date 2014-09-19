#!/usr/bin/env python
# coding: utf-8
try:
    from cracklib import FascistCheck, VeryFascistCheck
except ImportError:
    pass
else:
    from django.core.exceptions import ValidationError

    def cracklib_fascist_check_password_validator(password):
        try:
            FascistCheck(password)
        except ValueError as e:
            raise ValidationError(e.message)

    def cracklib_very_fascist_check_password_validator(password):
        try:
            VeryFascistCheck(password)
        except ValueError as e:
            raise ValidationError(e.message)