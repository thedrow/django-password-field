#!/usr/bin/env python
# coding: utf-8
from django.db import models
from password_field import fields
from password_field.validators import cracklib_fascist_check_password_validator


class Foo(models.Model):
    password = fields.PasswordField()
