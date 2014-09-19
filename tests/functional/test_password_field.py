#!/usr/bin/env python
# coding: utf-8
from django.test import SimpleTestCase
from faker import factory

from tests.support.models import Foo


class PasswordFieldTestCase(SimpleTestCase):
    faker = factory.Factory.create()

    def test_foo_saves_password(self):
        expected = self.faker.password()

        foo = Foo(password=expected)
        foo.save()

        foo = Foo.objects.get(pk=foo.pk)

        self.assertEqual(foo.password, expected)

