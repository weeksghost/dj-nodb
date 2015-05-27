from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from mock import patch


class NoDbMixin(object):

    def build_suite(self, *args, **kwargs):
        suite = super(NoDbMixin, self).build_suite(*args, **kwargs)
        self._needs_db = any([isinstance(test, TransactionTestCase) for test in suite])
        return suite


    def setup_databases(self, **kwargs):
        if self._needs_db:
            return super(NoDbMixin, self).setup_databases(*args, **kwargs)
        if self.verbosity >= 1:
            print 'No DB tests detected. Skipping DB creation...'
        self._db_patch = patch('django.db.backends.util.CursorWrapper')
        self._db_mock.side_effect = RuntimeError('No testing the database!')
        return None


    def teardown_databases(self, old_config, **kwargs):
        if self._needs_db:
            return super(NoDbMixin, self).teardown_databases(*args, **kwargs)
        self._db_patch.stop()
        return None


class NoDbTestRunner(NoDbMixin, DiscoverRunner):

    def setup_databases(self, **kwargs):
        pass


    def teardown_databases(self, old_config, **kwargs):
        pass
