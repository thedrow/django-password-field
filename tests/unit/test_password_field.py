#!/usr/bin/env python
# coding: utf-8
from django.test import SimpleTestCase
from faker import factory

from tests.support.compat import mock


class PasswordFieldTestCase(SimpleTestCase):
    faker = factory.Factory.create()

    def test_password_field_is_settable_on_model(self):
        expected = self.faker.password()

        with mock.patch('tests.unit.support.models.fields.make_password') as mocked_make_password:
            from tests.support.models import Foo

            foo = Foo(password=expected)

        mocked_make_password.assert_called_once_with(expected)

    def test_password_is_compareable(self):
        expected = self.faker.password()

        with mock.patch('tests.unit.support.models.fields.check_password') as mocked_check_password:
            from tests.support.models import Foo

            foo = Foo()
            foo.password = expected

            foo.password == expected

        mocked_check_password.assert_called_once_with(expected, 'plain$$%s' % expected, setter=mock.ANY)

