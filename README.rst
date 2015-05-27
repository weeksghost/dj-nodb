dj-nodb
=======

Custom django testrunner that eliminates test database creation when running tests.

Installation
------------

* pip install dj-nodb

This will place the custom testrunner (runner.py) at the root of your project. Alternatively you can move it to any part of your application you desire.

Usage (default)
---------------

Override django's default testrunner by adding the following to your settings

``TEST_RUNNER = 'runner.NoDbTestRunner'``
or
``TEST_RUNNER = '<your_app>.runner.NoDbTestRunner'``
