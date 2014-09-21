#!/usr/bin/env python
# coding: utf-8
from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from faker import factory

from password_field.validators import cracklib_fascist_check_password_validator


class CracklibPasswordValidationTestCase(SimpleTestCase):
    faker = factory.Factory.create()

    def test_short_password_raises_validation_error(self):
        expected = 'a'

        with self.assertRaisesMessage(ValidationError, 'it is WAY too short'):
            cracklib_fascist_check_password_validator(password=expected)

    def test_simple_password_raises_validation_error(self):
        expected = 'abcdef'

        with self.assertRaisesMessage(ValidationError, 'it is too simplistic/systematic'):
            cracklib_fascist_check_password_validator(password=expected)

    def test_complex_password_raises_no_validation_error(self):
        expected = 'qwvmsa14@^'

        try:
            cracklib_fascist_check_password_validator(password=expected)
        except Exception as e:
            self.fail(e.message)
