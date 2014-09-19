#!/usr/bin/env python
# coding: utf-8
from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from faker import factory

from tests.support.models import CracklibFascistCheckModel


class PasswordValidationTestCase(SimpleTestCase):
    faker = factory.Factory.create()

    def test_short_password_raises_validation_error(self):
        expected = 'a'

        with self.assertRaises(ValidationError):
            CracklibFascistCheckModel(password=expected)
