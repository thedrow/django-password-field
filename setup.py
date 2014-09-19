try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-password-field',
    version='0.1.0',
    packages=['password_field'],
    url='https://github.com/thedrow/django-password-field',
    license='BSD3',
    author='Omer Katz',
    author_email='omer.drow@gmail.com',
    description=''
)
