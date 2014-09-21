#!/usr/bin/env python
# coding: utf-8
from django.utils.translation import ugettext_lazy as _

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

try:
    import zxcvbn
except ImportError:
    pass
else:
    class ZXCVBNValidator(object):
        message = _("Passwords must be at least %s characters and of sufficient complexity")
        code = "zxcvbn"

        def __init__(self, password_minimum_entropy=40):
            self.password_minimum_entropy = password_minimum_entropy

        def __call__(self, value):
            res = zxcvbn.password_strength(value)
            if res.get('entropy') < self.password_minimum_entropy:
                raise ValidationError(self.message % _("Password is too weak"), code=self.code)