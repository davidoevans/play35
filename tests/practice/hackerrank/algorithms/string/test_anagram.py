import pytest
from tests.base.base_test import pytest_generate_tests
from tests.base.base_test import BaseTest


scenario1 = ('sample', {'test_name': 'anagram', 'test_id': 'sample'})
scenario2 = ('1', {'test_name': 'anagram', 'test_id': '1'})


class TestAnagramWithScenarios(BaseTest):
    scenarios = [scenario1, scenario2]

    def setup_method(self, test_in_validate_out):
        self.filename = __file__

    def test_in_validate_out(self, test_name, test_id):
        super().test_in_validate_out(test_name, test_id)
