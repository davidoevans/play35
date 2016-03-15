import pytest
from tests.base.base_test import pytest_generate_tests
from tests.base.base_test import BaseTest

scenario1 = ('sample', {'test_name': 'grid_search', 'test_id': 'sample'})
# scenario5 = ('5', {'test_name': 'grid_search', 'test_id': '5'})


class TestFibonacciModifiedWithScenarios(BaseTest):

    scenarios = [scenario1]

    def setup_method(self, test_in_validate_out):
        self.filename = __file__

    def test_in_validate_out(self, test_name, test_id):
        super().test_in_validate_out(test_name, test_id)
