# -*- coding: utf-8 -*-
"""
dj-nodb
=======

Custom django testrunner that eliminates test database creation when running tests.

###Installation

* pip install dj-nodb

This will place the custom testrunner (runner.py) at the root of your project. Alternatively you can move it to any part of your application you desire.

###Usage (default)

Override django's default testrunner by adding the following to your settings

```python
TEST_RUNNER = 'runner.NoDbTestRunner'
```
or
```python
TEST_RUNNER = '<your_app>.runner.NoDbTestRunner'
```
"""

from setuptools import setup


setup(
    name='dj-nodb',
    version='0.0.1',
    description='custom django testrunner',
    url='https://github.com/weeksghost/dj-nodb',
    author='Erik Marty',
    author_email='erikomarty@yahoo.com',
    license='Apache',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['mock']
)
